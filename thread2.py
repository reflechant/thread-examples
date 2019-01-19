import threading
import time

N = 100000000
thread_num = 10


def f(l, a, b):
    l.append(sum(range(a, b)))

def sumpar():
    l = []
    threads = []
    t1 = time.clock()
    for i in range(thread_num):
        t = threading.Thread(target=f, args=(l, i*N//thread_num, (i+1)*N//thread_num))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(sum(l))
    t2 = time.clock()

    print("потоки:", t2 - t1)


def sumseq():
    t1 = time.clock()
    print(sum(range(1, N)))
    t2 = time.clock()
    print("последовательно:", t2 - t1)

sumpar()
sumseq()