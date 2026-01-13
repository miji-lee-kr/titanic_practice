class writer():
    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method
        self.file_obj = None # 아직 자원 안들어옴
                            # 받는 인자 목록에 없어도 생성자일 수 있음
        
    def __enter__(self):
        self.file_obj = open(self.file_name, self.method) # 진입 포인트. 오픈 함수
                                                # 버전2 with 동일하게 open(파일명, 읽기전용) 받음
        return self.file_obj 
    
    
    def __exit__(self, exeption_type, value, trace_back): # 역할: 1. with 실행 중 (write 중) 에러 났으면 예외 뱉어낼지, 경미한거면 그냥 무시할지 결정해줘
                                                        # 역할 2: 열린 파일 닫아줘
    # with writer 돌릴때 생긴 예외를 파이썬이 잡아서 __exit__에 전달 -> return False로 직접 내려감
    # with 문은 애초에 예외 발생 디테일을 전달하는 구조. __exit__는 그걸 받아 어떻게 처리할지 뱉어내는 고조
        
        if self.file_obj is not None: # 자원 획득했다면. else는 자원 자체가 없으니 정리할 것도 없어 암것도 안함
            try:
                self.file_obj.close() 
            except Exception: # 닫는 중 문제 생겼다면 pass로 무시함 - 닫는 중 생긴 에러는 무시하지만, 실행중의 에러는 return False로 바로 알려줌
                pass

        return False  # 예외 처리의 True: 이 클래스가 조용히 무시하겠다 (처리 = yes).
                        # 예외 처리의 False: 이 클래스에서 처리 안하고 알람 보내겠다 (처리 =false)

                
with writer('./testfile.txt', 'w') as f: # class와 같은 이름 with 로 실행
    f.write('Test')
    
# __enter__로 진입해서 f.write('test')쓰고 __exit__로 나감