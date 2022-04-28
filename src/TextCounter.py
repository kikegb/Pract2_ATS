import multiprocessing as mp
from multiprocessing import Pool
import sys
from MapReduce import MapReduce

NUM_PROC = 2
lista = range(100000)

def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

def bucle_chulo(line):
        letter_freq = {}
        for letter in line:
            if letter.isalpha():
                if letter_freq.get(letter) is not None:
                    letter_freq[letter] = letter_freq[letter] + 1
                else:
                    letter_freq[letter] = 1
        print(letter_freq)

def main(file_path):
    mr = MapReduce(file_path)
    mr.map()

if __name__ == "__main__":
    print("Number of cpu : ", mp.cpu_count())
    main(sys.argv[1])
