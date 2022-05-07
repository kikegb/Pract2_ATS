from multiprocessing import Pool

class MapReduce:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = self.read_file(file_path)
        self.result = []
        self.total_words = 0
        self.map()
        self.shuffle()
        self.reduce()
        self.calculatePercent()
        self.printResult()

    """Funció map(): Crea els threads per a l'execució de sort()"""
    def map(self):
        p = Pool()
        result = p.map(self.sort, self.file_content)
        for x, y in result:
            self.result.append(x)
            self.total_words += y

    """Funció sort(): a partir d'un string, crea un diccionari amb la frequencia de paraules per lletra"""
    def sort(self, line):
        words = line.split(" ")
        letter_freq = {}
        total_words = 0
        for word in words:
            found_dict = {}
            total_words += 1
            for letter in word.lower():
                if letter.isalpha():
                    if letter not in found_dict.keys():
                        found_dict[letter] = True
                        if letter not in letter_freq.keys():
                            letter_freq[letter] = [1]
                        else:
                            letter_freq[letter][0] += 1
        return letter_freq, total_words

    """Funció shuffle(): uneix els resultats de map() a un únic diccionari amb clau=lletra i 
    valor=llista de frequencies de la lletra a cada thread"""
    def shuffle(self):
        letter_freq = {}
        for x in self.result:
            for k, v in x.items():
                if k in letter_freq.keys():
                    letter_freq[k].append(v[0])
                else:
                    letter_freq[k] = v
        self.result = letter_freq

    """Funció reduce(): suma dels valors de frqüencies per a cada lletra al diccionari del resultat de shuffle()"""
    def reduce(self):
        for k, v in self.result.items():
            letters_in_file = 0
            for numbero in v:
                letters_in_file += numbero
            self.result[k] = letters_in_file

    """Funció calculatePercent(): calcula percentatges a partir del resultat de reduce() i el nombre total de paraules al fitxer"""
    def calculatePercent(self):
        for k, v in self.result.items():
            self.result[k] = round((v / self.total_words) * 100, 2)

    """Funció per llegir el fitxer"""
    def read_file(self, path):
        f = open(path, 'r', encoding='latin-1')
        lines = f.readlines()
        f.close()
        return lines

    """Funció per mostrar i formatejar el resultat per pantalla"""
    def printResult(self):
        print(self.file_path + ":")
        for k, v in self.result.items():
            print(str(k) + " : " + str(v) + "%")
        print("\n")
