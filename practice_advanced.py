# futures + as_completed (스레드 당 작업 시간 상한)

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed  


work_list = [100000,1000000, 10000000] # 계산이 많은 CPU 작업
                            # 스레드 1은 첫번째 1000, 스레드 2는 10000 각자 일 어사인됨
                            # 스레드가 각각 동시에 일하는 것을 기대
def sum_gen(n):
    return sum(n for n in range(1, n+1))

def main():
    threads = min(10, len(work_list))
    start_time = time.time()
    
    future_list = []

    with ThreadPoolExecutor() as executor: 
        for work in work_list:
            future = executor.submit(sum_gen, work) # Future 객체 반환 
                                                #  Future(task1), Future(task2),.. 생성
                                                # executor: 작업 접수 + 배분 데스크
                                                # submit(): 작업 접수표 발급
                                                # Future: 번호표 (나중에 결과 찾으러올때 필요) 
            future_list.append(future) 
            print('Scheduled for {}:{}'.format(work, future)) # 예정 작업들 확인
        result = wait(future_list, timeout = 5) # 작업 시간 각 5초 줌
        
        print('Successful tasks: '+ str(result.done)) # 성공 작업들
    
        print('Pending tasks: '+ str(result.not_done)) # 실패 작업들
        
        print([future.result() for future in result.done]) # 성공 태스크의 결과값 (합계)

    end_time = time.time()
    msg = 'Running Duration: {:.2f}s'
    print(msg.format(end_time - start_time))
    
    
if __name__== '__main__':
    main()  
    