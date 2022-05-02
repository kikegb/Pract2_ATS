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

def main(file_path):
    mr = MapReduce(file_path)

if __name__ == "__main__":
    print("Number of cpu : ", mp.cpu_count())
    main(sys.argv[1])
