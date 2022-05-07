#!/usr/bin/python3

from multiprocessing import Pool
import sys

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


    def map(self):
        p = Pool()
        result = p.map(self.sort, self.file_content)
        for x, y in result:
            self.result.append(x)
            self.total_words += y

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

    def shuffle(self):
        letter_freq = {}
        for x in self.result:
            for k, v in x.items():
                if k in letter_freq.keys():
                    letter_freq[k].append(v[0])
                else:
                    letter_freq[k] = v
        self.result = letter_freq


    def reduce(self):
        for k, v in self.result.items():
            letters_in_file = 0
            for numbero in v:
                letters_in_file += numbero
            self.result[k] = letters_in_file

    def calculatePercent(self):
        for k, v in self.result.items():
            self.result[k] = round((v / self.total_words) * 100, 2)

    def read_file(self, path):
        f = open(path, 'r', encoding='latin-1')
        lines = f.readlines()
        f.close()
        return lines

    def printResult(self):
        print(self.file_path + ":")
        for k, v in self.result.items():
            print(str(k) + " : " + str(v) + "%")
        print("\n")

if __name__ == "__main__":
    for file_num in range(1,len(sys.argv)):
        MapReduce(sys.argv[file_num])
