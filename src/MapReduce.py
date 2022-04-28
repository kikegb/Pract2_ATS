import numpy as np
from multiprocessing import Pool

class MapReduce:

    def __init__(self, file_path):
        self.file_content = self.read_file(file_path)
        self.letter_count = {}

    def mapReduce(self):
        map_result = self.map(self.file_content)
        shuffle_result = self.shuffle(map_result)


    def map(self, file_lines):
        p = Pool(len(file_lines))
        result = p.map(self.sort, file_lines)
        return result

    def sort(self, line):
        letter_freq = {}
        for letter in line:
            if letter.isalpha():
                if letter_freq.get(letter) is not None:
                    letter_freq[letter] = letter_freq[letter] + 1
                else:
                    letter_freq[letter] = 1
        return letter_freq

    def shuffle(self, map_lines):
        letter_freq = {}
        for x in map_lines:
            """Juntar diccionarios (key: letra, value: listas de 1's"""
        return letter_freq


    def reduce(self):
        """Calcular total frequencia letras"""
        """Calcular porcentages"""
        pass

    def read_file(self, path):
        f = open(path, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        return lines

    def write_file(self, path):
        pass