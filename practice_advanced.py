# 여러 스레드 만들기

import logging
import time
from concurrent.futures import ThreadPoolExecutor

def task(name):
    logging.info('Sub-thread %s: Start', name)
    
    result = 0
    for i in range(100):
        result = result +i
        
    logging.info('Sub-thread %s: Finish %d', name, result) # %d: 정수형 (decimal)
    return result


def main():
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level = logging.INFO, datefmt = '%H:%M:%S')
    logging.info('Main thread - Before creating & running thread')
    
    
    # 방법 1
    
    # executor = ThreadPoolExecutor(max_workers= 3) # 워커수 = 스레드 생성 수
    # 작업 성격에 맞게 워커수 직접 설정 추천
    # I/O 작업 많으면: 작업 갯수와 동일 갯수 스레드면 CPU 놀고 있으니 워커수 늘림. 작업수 *5-20
    # CPU 작업 많으면: 스레드 갯수 많으면 queue에 줄서있는 스레드에도 번갈아가며 기회 주느라 시간 오래 걸리고 비용 높아짐 (context switching)    
    # 작업수 = 워커수
    
    # task1 = executor.submit(task, ('1st'))
    # task2 = executor.submit(task, ('2nd'))
    
    # print(task1.result())
    
    
    
    # 방법 2
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['1st', '2nd'])
        print(list(tasks))

if __name__=='__main__':
    main()