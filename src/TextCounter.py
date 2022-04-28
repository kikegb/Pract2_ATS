import multiprocessing as mp
from multiprocessing import Pool
import sys;

NUM_PROC = 2

lista = range(100000)

def bucle_chulo(lista):
    for i in lista:
        print("HOLA" + str(i))

def main():
    file = read_file(sys.argv[0])
    p = Pool(3)
    p.apply(bucle_chulo, lista)

if __name__ == "__main__":
    print("Number of cpu : ", mp.cpu_count())
    for i in range(2):
        main()
    jobs = []

def read_file(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines
