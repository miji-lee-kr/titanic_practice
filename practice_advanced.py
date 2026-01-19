# 요구조건: 5개의 서브 프로세스를 Process로 만들고 돌려라. 서브 프로세스는 n *n 이어야한다. 서브 프로세스의 생명 주기에 신경 써라


from multiprocessing import Process
import logging
import time
import os


def func(arg):
    # logging.info('Sub thread started: n%s', {arg})
    # logging.info(arg)
    print('Sub thread started: ', arg, os.getpid())
    print(arg * arg)

def main():
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level = logging.INFO, datefmt = '%H:%M:%S')
    process_id = os.getpid()
    processes = []
    for p in range (5):
    
        process = Process(target = func, args = (p,))
        processes.append(process)
        process.start()
    logging.info('Main proccess joined', process_id)
    for p in processes:
        p.join()
    logging.info('Main process is over')

if __name__ == '__main__':
    main()