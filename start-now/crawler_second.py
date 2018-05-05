# coding=utf-8
# 分布式爬虫基础

# 多线程 threading
'''import threading      
def thread_job():
    print('这个线程是：%s' % threading.current_thread())


def main():
    thread = threading.Thread(target=thread_job())
    thread.start()


if __name__ == '__main__':
    main()'''     # 多线程基础创建线程

'''import threading
import time

def thread_job1():
    print("T1 启动\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 完成")

def thread_job2():
    print("T2 启动")
    print("T2 完成")

thread1 = threading.Thread(target=thread_job1(), name= 'T1')
thread2 = threading.Thread(target=thread_job2(), name= 'T2')
print(threading.current_thread())
thread1.start()
thread2.start()
thread2.join()
thread1.join()

print("all done")'''     # 多线程join   当一个进程启动时会产生一个主进程，我们手动创建的均为子进程，
#  （1）主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束
#  （2）设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止

'''thread = threading.Thread(target=thread_job())
thread.start()
thread.join()
print("all done")'''

'''import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)    # 多线程调用的函数不能使用return返回数值


def mult_thearding():
    q= Queue()  # 存放返回值
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]

    for i in range(4):
        t = threading.Thread(target=job(data[i], q))          
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []

    for i in range(4):
        result.append(q.get(i))

    print(result)


if __name__ == '__main__':
    mult_thearding()'''  # 线程锁 lock  在每个线程运行修改内存之前，运行lock.acquire（）将共享内存上锁，
           # 确保当前内存执行时，内存不会被其他线程访问


'''import multiprocessing as mp


def job(q):
    a = 1
    for i in range(10):
         a += a

    q.put(a)


if __name__ == '__main__':
    q = mp.Queue()

    p = mp.Process(job(q))
    p.start()
    p.join()

    res = q.get()
    print(res)'''  # 进程使用 QUEUE

import multiprocessing as mp

def job(x):
    return x * x


def mulitprocess():
    pool = mp.Pool()

    res = pool.map(job, range(5))

    print(res)

if __name__ == '__main__':
    mulitprocess()
