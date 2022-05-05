#!/usr/bin/python3
import multiprocessing as mp
from multiprocessing import Pool
import sys
from MapReduce import MapReduce

def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

if __name__ == "__main__":
    for file_num in range(1,len(sys.argv)):
        MapReduce(sys.argv[file_num])
