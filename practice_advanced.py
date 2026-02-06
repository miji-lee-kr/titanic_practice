# 상속
# 기존 설계를 유지하면서, 새로운 요구사항에 맞게 변화를 주고 싶을 때


class Robot: 
    population = 0 
    
    def __init__(self, name):
        self._name = name   
        Robot.population += 1 
        
        
    @classmethod  
    def class_name(cls):
        print(f'In {cls}: Total {cls.population} Robots')
        
        
    @staticmethod 
    def is_this_robot():
        print("yes")
        
    
    def cal_add(self,a,b): # a,b는 객체 생성시 필요한게 아니고 이미 생성된 객체가 부를 때만 필요하니 __init__에서 정의 안해줘도 됨
        return a*b
    

    def __str__(self): 
        return f'Robot name: {self._name}'
        
 
# 부모 상속
class Siri(Robot):  
    # population = 0
    
    
    # 매직메소드 오버라이딩
    def __init__(self, name, age): # 새 인자 age 추가는 가능해도 물려진 인자 name은 뺄 수 없음
        super().__init__(name) # super(): 부모의 __init__ 설정 그대로 둔 채로 가져와서 + 자식 클래스에서 확장하고 싶을 때
        self._age = age 
        Siri.population += 4
    
    def cal(self,a):
        a = 3
        return a
    
    # 일반함수 오버라이딩 
    @classmethod
    def class_name(cls): # 클래스 이름은 Robot 이 아닌 Siri라고 함.
        print(f'Overrided: {cls}')   
        
    
    def cal_mult(self,a,b):
        return self.cal(a)+ super().cal_add(a,b) # 메소드 return안에 다른 메소드를 사용할 수 있음 (참조된 메소드가 return으로 값을 반환했을 경우만. print면 반환할 값 없어서 안됨)
    
    
bixby = Robot('Bixxy') 
siri = Siri('iphone', 11) 


print(siri) # 부모가 가진 함수 __str__ 상속받아 실행됨
siri.is_this_robot() # return 이 없으므로 print()하면 None 리턴
siri.class_name() # 부모 클래스의 class method 불러도 Siri 가 클래스라고 함
                # population이 자식에게 없을때는 부모의 population을 가져왔으나 자식에게 생기니 자식 것이 덮어쓰기 되서 가져와짐
                
# print(siri._a)  # a는 cal 불러야만 존재하기 시작함. cal 안부른 상태에서 a 부르면 에러 -> __init__생성자안에 인자들은 애초에 다 저장해둬야

Robot.class_name()  # Siri 클래스 안에서 Robot.population을 고치면 Robot.class_name()으로 불러도 숫자가 바뀌어버림
print(siri)

print(siri.cal_mult(10,20))