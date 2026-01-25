# 멀티프로세스 버전
# 멀티프로세스 /asyncio/ 멀티스레드 바꿔도 코드 변동이 크지 않으므로 하나씩 짜서 실행시간 측정해서 짧은 것 선택 추천

import multiprocessing
import requests 
import time

session = None


def set_global_session():
    global session # 각 프로세스 메모리 영역에 함수 실행할때마다 객체 생성은 비싸다 -> global 써서 각 프로세스마다 할당하도록 (공유와 다름)
    # 
    if not session:
        session = requests.Session()


def request_website(url):
    print(session) # 세션을 여러번 돌려쓰는 것 보임
    with session.get(url) as response:
        print(f'[Read Content: {len(response.content)}, Status code: {response.status_code}], from {url}')
        
    
    
    
# 실행함수 2. 요청
def request_all_website(urls):
    with multiprocessing.Pool(initializer= set_global_session, processes = 4) as pool:
        pool.map(request_website, urls) # 풀, 동시성에서는 순서 보장 x
    
    

def main():
    urls = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
        "http://realpython.com"
    ] * 3 

    start_time = time.time()
    request_all_website(urls)
    
    duration = time.time() - start_time
    print(f'Downloaded {len(urls)} sites in {duration} seconds')
    

if __name__ == '__main__':
    main()