import threading
import time
from queue import Queue


# 将工作的数据列表传入queue返回
def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l) # 多线程使用函数返回值时无法使用return


def multhreading():
    q = Queue()
    #thread = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
    #  thread.append(t)
        t.join()
    # print(thread)
    resluts =[]
    for _ in range(4):
        resluts.append(q.get())
    print(resluts)


if __name__ == '__main__':
    multhreading()

