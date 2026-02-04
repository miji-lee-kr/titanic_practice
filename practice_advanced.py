# asyncIO 기초
# 비동기식 처리

from multiprocessing import current_process, Array, Manager, Process
import time
import os

def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    print(f'Process ID: {process_id}, Process name: {process_name}')
    total_list.append(sum(i*i for i in range (number)))

def main():
    numbers = [3000000 +x for x in range(30)]
    processes = list()
    manager = Manager()
    
    total_list = manager.list()
    
    start_time = time.time()
    for i in numbers:
        t = Process(name= str(i), target = cpu_bound, args = (i, total_list,))
        processes.append(t)
        t.start()
    
    for process in processes:
        process.join()
        
    print(total_list)
    duration = time.time() - start_time
    print(f'{duration} seconds')
if __name__ == '__main__':
    main()