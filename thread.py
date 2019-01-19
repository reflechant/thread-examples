import threading
import requests
import time


def f(i):
    t1 = time.clock()
    requests.get("https://google.ru")
    t2 = time.clock()
    print(t2 - t1)


l = []
t1 = time.clock()
for i in range(10):
    t = threading.Thread(target=f, args=(i, ))
    l.append(t)
    t.start()

for t in l:
    t.join()
t2 = time.clock()

print("Всё,", t2 - t1)
