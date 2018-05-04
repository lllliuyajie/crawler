import threading
import time

def thread_job():
    '''print("This is a thread of " + str(threading.current_thread()))'''
    print("T1 started\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finished\n")


def main():
    add_threading = threading.Thread(target=thread_job)
    add_threading.start()
    add_threading.join()
    print("all done\n")
    '''print(threading.activeCount())
    print(threading.enumerate())
    print(threading.current_thread())'''


if __name__ == '__main__':     # python模拟程序入口 当引入别的模块时，可以不执行引入模块中的文件
    main()
