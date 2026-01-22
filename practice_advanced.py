# blocking I/O : 인풋아웃풋 완료시까지 응답 대기. 다음 코드 실행 불가
# 제어권이 I/O 작업에 잇음 -> 커널로 제어권 옮겨감 -> 응답 전까지 대기하는동안 제어권 잃음 -> 다른 작업 수행 불가

# non-blocking I/O: 커널 IO 작업 완료 여부 상관 없이 즉시 응답
# 제어권I/O -> 유저 프로세스 -> 다른 작업 지속 가능 -> 주기적으로 시스템 콜로 IO 작업 여부 확인

# Async vs. Sync
# async: IO 작업 완료 여부에 대한 알림은 커널 -> 유저 프로세스. call back 함수로
# sync: 알림은 유저 프로세스 -> 커널 (호출되는 함수)

# async + non_block IO/ block IO
# sync + non_block IO / block IO



import concurrent.futures
import threading
import requests 
import time

# 멀티 스레드 예제 (3초)가 순차실행 코드 (4초)보다 더 빠름

# 각 스레드에 생성되는 객체 - 전역에 선언
# 스레드는 변수를 공유하지만 각 스레드마다 동일한 이름의 별도의 변수로 쓰고 싶을 때
thread_local = threading.local()
# 각 스레드에 별도의 독립적 네임 스페이스 메모리 영역 할당받아 사용


def get_session():
    if not hasattr(thread_local, 'session'): # 워커가 지난 스레드 작업으로 이미 session을 갖고 있다면
        thread_local.session = requests.Session()
    return thread_local.session



def request_website(url):
    session = get_session()
    print(session) # 세션을 여러번 돌려쓰는 것 보임
    with session.get(url) as response:
        print(f'[Read Content: {len(response.content)}, Status code: {response.status_code}], from {url}')
        
    
    
    
# 실행함수 2. 요청
def request_all_website(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
        executor.map(request_website, urls)

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