from threading import Thread
from time import sleep, time


def download(file_name):
    print("Downloading file...", file_name)
    sleep(0.5)
    print("Download complete")


if __name__ == "__main__":

    files = ["vedio.mp4", "image.png", "data.csv"]
    start = time()
    for f in files:
        download(f)
    end = time()
    print(f" serial time {end - start:.2f} seconds")

    start = time()
    threads = []
    for f in files:
        t = Thread(target=download, args=(f,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time()
    print(f" parallel with threads time {end - start:.2f} seconds")

    print("Bye")
