# from multiprocessing import Process, current_process, Value, Array
# import os
# from concurrent.futures import ProcessPoolExecutor

# shared_value = 0

# def update_number(v):
#     v = shared_value
#     v.



    
# def main():
#     process_id = os.getpid()     # 메인 프로세스 ID는 디버깅을 위해 필수
#     print(f'Process ID {process_id}')
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         futures = executor.submit(target = update_number) 
#         futures.result()    
#     print('Final data in original process', shared_value)

        
# if __name__ == '__main__':
#     main()
    
    
    
    

from multiprocessing import Process, Queue, current_process
import time
import os
from concurrent.futures import ProcessPoolExecutor



def worker(q, num):
    # 각자가 숫자 만든다.
    # 그리고 하나에 넣느다
    value= 0
    for i in range(num):
        value +=1
    q.put(value)
    q.put('Exit')
    
def main():
    # worker를 참고하는 processpool 만든다.
    l = []
    q = Queue()
    for i in range(5):
        p = Process(target = worker, name = i, args = (q,i))
        l.append(p)
    for j in l:
        j.join()
        
        
    # queue를 만든다
    # queue에서 만든것을 빼서 더한다
    #제동 걸어준다
    exit_cnt = 0
    total_cnt = 0
    while exit_cnt <len(l):
        if q.get() =='Exit':
            exit_cnt +=1 
        else: 
            total_cnt += q.get() 
        

if __name__ == '__main__':
    main()