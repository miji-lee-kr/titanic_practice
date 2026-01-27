# race condition 
# 

import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self,n):
        logging.info('Thread %s, %d: Starting update', n, self.value)
        
        
        with self._lock: # lock acquire 과 return 을 자동으로 해줌
            logging.info('Thread %s acquires lock', n)
            local_copy = self.value  
            local_copy += 1 
            time.sleep(0.1)
            self.value = local_copy
            logging.info('Thread %s: Finished update. Current value %d', n, self.value)
        

if __name__   == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level = logging.INFO, datefmt = '%H:%M:%S')
    store = FakeDataStore()
    logging.info('Testing update. Starting value %d', store.value)
    
    with ThreadPoolExecutor(max_workers= 3) as executor:
        for n in ['1st', '2nd', '3rd']:
            executor.submit(store.update, n)
            
    logging.info('Testing update. Ending value %d', store.result())