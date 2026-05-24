from threading import Thread
from time import sleep, time
from multiprocessing import Process


def calculate(n1, n2):
    sum = 0
    for n in range(n1, n2):
        sum += n * n


if __name__ == "__main__":

    num = 50_000_000

    calculate(0, num)

    mid = num // 2

    t1 = Thread(target=calculate, args=(0, mid))
    t2 = Thread(target=calculate, args=(mid, num))

    start = time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print(f" parallel with threads time {end - start:.2f} seconds")

    t1 = Process(target=calculate, args=(0, mid))
    t2 = Process(target=calculate, args=(mid, num))

    start = time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print(f" parallel with processes time {end - start:.2f} seconds")

    print("Bye")
