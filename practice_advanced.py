from multiprocessing import Process, Pipe, current_process
import time
import os


def worker(id, baseNum, p):
    process_id = os.getpid()
    process_name = current_process().name
    sub_total = 0
    
    for i in range(baseNum):
        sub_total += 1
        
    p.send(sub_total)
    p.close()    
    
    print(f'Process ID: {process_id}, Process Name: {process_name}, ID: {id}')
    print(f'Result: {sub_total}')

    
def main():
    process_id = os.getpid()
    print('Main process ID', process_id)

    start_time = time.time()          
    
    main_p, sub_p = Pipe()
    
    # pipe는 메인과 서브 간 1:1 통신이므로 for 지움
    t = Process(name = str(1), target = worker, args = (1, 100000, sub_p))

    t.start()      
        
    t.join()
        
    print('----- %s seconds-----' % (time.time() - start_time))
    
    
        
    print('Main-processing2 Done. Main-process Total count = {}'.format(main_p.recv()))
     
        
if __name__ == '__main__':
    main()
    
    
    # 5개의 추가 프로세스가 나눠서 작업한 값을 queue 에 보내고, 기존 프로세스가 queue 에서 받아서 total+= tmp 에서 총합
