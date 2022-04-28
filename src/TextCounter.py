import multiprocessing as mp
from multiprocessing import Pool
NUM_PROC = 2

lista = range(100000)

def bucle_chulo(lista):
    for i in lista:
        print("HOLA" + str(i))

def main():
    p = Pool(3)
    p.apply(bucle_chulo, lista)

if __name__ == "__main__":
    print("Number of cpu : ", mp.cpu_count())
    for i in range(2):
        main()
    jobs = []

