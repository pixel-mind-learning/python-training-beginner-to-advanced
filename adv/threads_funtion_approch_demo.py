# function approach is the pythonic way

from time import sleep
from threading import Thread


def hello():
    for i in range(5):
        print("Hello ", i + 1)
        sleep(0.3)


def hi():
    for i in range(5):
        print("Hi ", i + 1)
        sleep(0.3)


if __name__ == "__main__":
    t1 = Thread(target=hello)
    sleep(0.2)
    t2 = Thread(target=hi)

    t1.start()
    t2.start()

t1.join()
t2.join()

print("Bye")
