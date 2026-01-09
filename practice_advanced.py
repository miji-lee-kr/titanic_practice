# futures + as_completed (스레드 당 작업 시간 상한)

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed  


work_list = [100000,1000000, 10000000] # 어떤 작업부터 먼저 스케줄링 될지는 랜덤
                    # 먼저 끝나는 것부터 나옴
def sum_gen(n):
    return sum(n for n in range(1, n+1))

def main():
    threads = min(10, len(work_list))
    start_time = time.time()
    
    future_list = []
    
    # 결과 건수
    with ProcessPoolExecutor() as executor:
        for work in work_list:
            future = executor.submit(sum_gen, work)
            future_list.append(future)
            print('Scheduled for {}: {}'.format(work, future))
            
        # as_completed 결과 출력    
        for future in as_completed(future_list): # wait과 달리 먼저 처리된 것부터 나옴
            result = future.result() 
            done = future.done()
            cancelled= future.cancelled
            
        # future 결과 확인
            print('Future Result: {}, Done: {}'.format(result, done))
            print('Future Cancelled: {}'.format(cancelled))

    end_time = time.time()
    msg = 'Running Duration: {:.2f}s'
    print(msg.format(end_time - start_time))
    
    
if __name__== '__main__':
    main()  
    
    
    
    
    
    
    
