# 생산자 소비자 패턴 producer consumer pattern
# queue를 사이에 두고 producer와 consumer가 협업
# data에 동시에 접근해서 망가질 수 있으니 queue에 담아놓은 걸 한 스레드가 접근해서 꺼내도록


# producer 조건: 끝나기 전까지 / 
# 
import logging
import concurrent.futures
import time
import threading
import queue
import random


# 데이터 만드는 생산자. (네트워크 대기상태 I/O 일 경우 등)
def producer(q, e): # 쌓이면 queue는 자동으로 조절해준다는데 왜 while 조건이 필요?
    while not e.is_set():
        v = random.randint(1,5)
        q.put(v)
    
# 데이터 받고 사용하는 소비자 (받아서 DB에 저장 등)
def consumer(q, e):
    while not e.is_set() or not q.empty():
        num = q.get()
        logging.info('Answer : %s, size = %d', num, q.qsize())
        
    
if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level = logging.INFO, datefmt = '%H:%M:%S')
    q = queue.Queue(maxsize=10)
    e = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, q,e) # q,e를 이 futures에도 공유하겠다
        executor.submit(consumer, q,e)
        time.sleep(1)
        e.set()
        
        
