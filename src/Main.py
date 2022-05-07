#!/usr/bin/python3

from MapReduce import MapReduce
import sys

if __name__ == "__main__":
    for file_num in range(1,len(sys.argv)):
        MapReduce(sys.argv[file_num])
