from time import sleep
from threading import Thread


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello ", i + 1)
            sleep(0.3)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi ", i + 1)
            sleep(0.3)


if __name__ == "__main__":
    t1 = Hello()
    sleep(0.2)
    t2 = Hi()

    t1.start()
    t2.start()

t1.join()
t2.join()

print("Bye")
