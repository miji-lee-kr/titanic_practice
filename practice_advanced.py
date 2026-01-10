import asyncio
import timeit
from urllib.request import urlopen # urlopen은 blocking I/O 함수. 코루틴 I/O 끝날때까지 다른 코루틴으로 못바꿈
                                # 근데 asyncio는 I/O 중 다른 코루틴으로 변경 가능 (non-blocking) -> 안맞음
                                # 블로킹 함수는 스레드 풀에 떠넘김
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading


start = timeit.default_timer()
urls = ['http://naver.com', 'http://idpaper.com']


async def fetch(url, executor): #
    loop = asyncio.get_running_loop() # 이벤트 루프 초기화
    response = await loop.run_in_executor(executor, urlopen, url) # url 블록함수를 여기서 non-block으로 만듦
                                                        # loop은 main영역에서 만들었으니 여기서도 참고 가능
                                                        # 이벤트 루프가 말함 “이 블로킹 함수는 저쪽 스레드에서 돌려” & Future response 하나를 즉시 받음
                                                        # loop.가 붙는 이유는 “이 일을 어떤 누가 관할하느냐”를 명확히 -> loop (이벤트 루프)가 한다


    return response.read()[0:5]
    


async def main(): # 돌아주는 스레드 생성해서 async로 넘김
    executor = ThreadPoolExecutor(max_workers=10)
    futures = [
        asyncio.create_task(fetch(url, executor)) for url in urls # url당 한 스레드 
             ]
    
    result = await asyncio.gather(* futures) # list 언패킹
    #gather가 하는 일

# 여러 awaitable(Task/Coroutine)를 받는다
# 모두 완료될 때까지 대기한다 (모은다 = gather)
# 완료되면 결과를 리스트로 반환한다
    
    
    print(result)
    duration = timeit.default_timer - start
    print('Running Duration: ', duration)



if __name__ == '__main__':
    asyncio.run(main())
