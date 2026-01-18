# 생산자 소비자 패턴 producer consumer pattern
# queue를 사이에 두고 producer와 consumer가 협업
# data에 동시에 접근해서 망가질 수 있으니 queue에 담아놓은 걸 한 스레드가 접근해서 꺼내도록

import logging
import concurrent.futures
import time
import threading
import queue
import random

# 데이터 만드는 생산자. (네트워크 대기상태 I/O 일 경우 등)
def producer(queue, event):
    while not event.is_set(): # event.set (멈추라는 신호)이 켜지지 않은 한 계속 수집
        message = random.randint(1,5)
        logging.info('Producer got message: %s', message)
        queue.put(message) # queue에 넣음
    logging.info('Producer sending event') 
    
    
# 데이터 받고 사용하는 소비자 (받아서 DB에 저장 등)
def consumer(queue, event):
    while not event.is_set() or not queue.empty(): # event.set이 켜지지 않거나 queue에 남은 한
        message = queue.get() # queue에서 가져옴
        logging.info('Consumer storing message: %s (size = %d)', message, queue.qsize()) 
    logging.info('Consumer received event')     
        
    
if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level = logging.INFO, datefmt = '%H:%M:%S')


    pipeline = queue.Queue(maxsize =10) # queue 객체 만듦 (이전에도 CPU 대기 상태에 task가 쌓였으나 이번에는 정식 queue 객체 생성하고 순서 지켜서 보관됨)
    # producer와 consuer사이 서로 데이터 주고받는 통신 담당
    # queue는 thread-safe + block 기능으로 값이 덮어써지는걸 막음

    # queue 사이즈 중요. 무조건 크면 좋지 않음

    
    event = threading.Event()  # 이벤트 플래그. 보내는 신호에 모든 스레드가 동시에 영향 받음

    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        
        time.sleep(0.1)  # 실행시간 조정 - while true동안 생산한다
                         # 백그라운드에서 메인 스레드는 계속 돌아가는 중. 메인이 sleep으로 0.1초 쉬는 (I/O) 동안 GIL은 CPU 일하는 워커에게 가고 한 스레드가 producer, consumer 번갈아 일함
        
        logging.info('Main about to set event')
        
        event.set() # 이벤트 켜는 신호가 모든 스레드의 while 문 끝내 수집/처리 종료
        # 내어쓰기 하면: 
        
        
# .Event() 플래그 핵심 기능 
# .set(): 이벤트 켜기 True. 켜지면 일 멈추는 신호로 해석
# .clear(): 이벤트 끄기 False
# .wait(): 이벤트 켜질 때까지 대기
# is_set(): 지금 이벤트가 켜져 있나 확인. 켜져 있으면 True