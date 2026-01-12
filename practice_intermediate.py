#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('a')


# In[ ]:


# 전역 변수 / 지역 변수

# 내 지역 안을 먼저 찾고 없으면 밖에 나가 찾음

b = 20

def bar():
    b =30
    return print(b)

bar()


# In[4]:


# 기본 사항 및 __repr__

class Car():
    
    # 클래스 변수
    # 이 클래스에서 생성되는 모든 인스턴스가 공유 - 모든 객체가 공통적으로 참조하는 값
    # 반면 인스턴스 변수, 메소드는 self(내 것)이므로 공유하지 않음

    def __init__ (self, brand, details): 
        self._brand = brand # self.로 시작하는 인스턴스 변수 
                            # 인스턴드 선언할 때는 구분 위해 _ 붙이는 습관 들이기
        self._details = details
        
    # print(car1) 할 때 class 정보 휴먼 리더블하게 출력 시키는 special method
    # __repr__ 메소드: 클래스 속성 정보를 보여줌. f-str 타입으로 변환시커야
    def __repr__ (self): # 모든 car 객체에 작동해야 하는 동작 부여 : 괄호 안 self 받는 인스턴스 메소드
        return f'Car(brand = {self._brand}, details = {self._details})'  
    
car1 = Car('Ferrari', {'colour':'white', 'price': 4000})
   
   
# 접근   
print(car1) # print하면 오브젝트만 나옴. special method로 class 정보 휴먼 리더블하게 출력 가능
print(car1.__dict__) # car1 속성 정보 체크
print(dir(car1)) # 사용 가능한 모든 메소드 + 변수들. 가져다 쓰면 됨


# In[ ]:





# In[5]:


# 클래스 변수 및 인스턴스 변수

class Car():
    car_count = 0    

    def __init__ (self, brand, details): 
        self._brand = brand 
        self._details = details
        Car.car_count += 1  # 한 객체 더해질 때마다 Car.__init__ 돌아감 -> car_count 추가됨 
                            # self.car_count += 1라고 하면 안됨. car1,car2 개별 car_count=1이 되고 전체 Car.car_count는 불변.
                            # car1.car_count =1                 
                
car1 = Car('Ferrari', {'colour':'white', 'price': 4000})
car2 = Car('BMW', {'colour':'silver', 'price': 3000})


# 접근
print(Car.car_count)
print(car1.car_count)
print(car2.car_count) # car_count는 모든 객체가 공유하므로 Car로 호출해도, car1로 호출해도 동일 


# In[6]:


# 클래스 메소드

class Car():

    increase_pct = 1.2

    def __init__ (self, brand, details): 
        self._brand = brand 
        self._details = details
    
    @classmethod
    def price_change (cls, pct): # pct는 여기서 정의되지 않고, 호출할 때 제시되는 숫자
        cls.increase_pct = pct

    def after_price(self):
        return f'Updated price : {self._brand}, {self._details.get('price')* Car.increase_pct} EUR'


car1 = Car('Ferrari', {'colour':'white', 'price': 4000})

car1.price_change(1.3)
print(car1.after_price())


# In[ ]:


# static method
# cls, self를 인자로 받지 않음 -> cls, self가 어떻든 상관 없는 로직. 
# cls, self의 설계 구조에 상관 없는 단순 계산, 유효성 판단등만 함  

class Car():
    def __init__ (self, brand, details): 
        self._brand = brand 
        self._details = details


    @staticmethod
    def is_bmw(brand): # 객체 중 _brand 부분만 빼서 BMW와 비교. static 메소드는 “이 값이 BMW인가만 판단. 객체가 있다는 사실조차 모름 
                    # 메소드가 객체/클래스 저장 공간에 직접 접근하면 → 인스턴드/클래스 메소드.
                    # 외부에서 값만 전달받으면 → 스테틱 메소드
        if brand == 'BMW':
            return 'Yes'
        return 'No' # 원래 이 줄은 if가 true여부에 상관없이 언제나 프린트되지만, if== true일 때 return 'yes'을 만나 수직 진행이 멈추고 'no' 프린트 안됨
   
#     @staticmethod     # 이 버전은 inst로 객체를 통째로 받기 때문에 static 아님. 그건 인스턴스 메소드
#     def is_bmw(inst):     # brand만 쓸거라면 애초에 inst._brand만 인자로 받아야했음
#     return inst._brand == 'BMW'


car1 = Car('BMW', {'colour':'white', 'price': 4000})


# 접근
print(Car.is_bmw(car1)) # car1 객체를 통째로 넣었으므로 false. 객체 전체 != 'BWW'이므로
Car.is_bmw(car1._brand) # car1 객체 중 brand만 넣었으므로 true


# In[ ]:


# special method : Fruit.eat(f1) 처럼 내가 "이름으로" 수동 호출해야 실행되는 메서드 말고, "특정 문법 실행시" 자동 호출되는 메서드
# __str__()같은 모양. 내가 만드는 일반 메서드는 연결된 문법이 없으므로 수동 호출해야

class Fruit:
        
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __repr__(self):
        return f'Class info {self._name}, {self._price}'
        
    def __sub__(self, other):
        return (other._price * self._price) / 3
    
    def eat (self):
        return print(self._name, "is yummy")

f1 = Fruit('orange', 100)
f2 = Fruit('banana', 500)

results = f2-f1
print(results) # 따로 Fruit.__sub__(f1,f2,f3) 특정 메소드로 안불러도 - 는 __sub__가 자동 실행되게 명령 내림.
# 연산 로직 커스터마이즈해서 새 기능 만들기 가능. 빼기 기호를 넣었는데 내부적으로는 곱하기 되도록 하는 것처럼

reaction = Fruit.eat(f1)


# In[ ]:


reaction = Fruit.eat(f1)


# In[ ]:


# 벡터 스페셜 메소드

class Vector():
    def __init__(self, *args): # x,y 한 쌍씩 들어오니까 묶음으로 패킹
        if len(args) == 0: # 예외처리
            self._x, self._y = 0,0 # 언패킹
        else:
            self._x, self._y = args
    def __repr__(self):
        return f'Vector ({self._x}, {self._y})'
    def __add__(self, new):
        return Vector(self._x + new._x, 
                      self._y + new._y) # 더한 결과로 새로운 Vector 객체 만든다 (어차피 더하면 새 숫자 = 새 객체 생성)
    def __bool__(self): # 하나라도 0보다 큰 원소 있으면 True
        return bool(max(self._x, self._y))
    
v1 = Vector(1,3)
v2 = Vector(10,2)
v3 = Vector()

print(v1+v3)   # 매직 메소드이므로 메소드를 호출하는 방법이 + - bool 
print(bool(v3))


# In[ ]:


# named tuple vs 보통 튜플

# 일반적인 튜플

u = ("miji", "Switzerland", 'ML engineer')
u[0] # name을 찾아야 하는데 몇번째 인덱스가 무슨 레이블이었나 잊어버림, 안보임 -> pain point


# 튜플은 함수등에서 생성되면 바로 변수로 언패킹되기 때문에 레이블 필요없음. 
def get_users():
    return 'miji', 'CH'

name, country = get_users() 


# In[ ]:


# tuple이 필요할 때 

# 튜플은 전달 단계에 최적화됨. 
# DB fetch 결과,API response 레코드, 로그/이벤트 등을 row 단위로 패킹되서 받고, 다른 시스템에 전달해줄 때 name, country등으로 언패킹
# 하지만 아직 쓸 방법을 모른채 오래 패킹된채로 들고 다니다보면 뭐가 뭐였는지 헷갈려짐. 
# 언패킹 되기 전까지 의미에 자주 접근해야하면 names tuple 만듦
# 그리고 named tuple은 (일반 튜플과 같이) 동작 코드를 위한 row 단위로 작동. 판다스 분석 코드는 column 단위로 데이터 처리를 위해 작동했지만 row단위는 프로그램 흐름 제어 목적 
# 판다스+apply 조합으로도 함수를 실행/동작할 수 있지만 고객 단위가 아니므로 (=row단위가 아니므로) 실행 순서 보장 ❌, 중간 실패 시 일부만 실행됨, 재실행하면 중복 메일, 테스트 거의 불가
# 동작 관점에서는 row가 ‘하나의 사건 단위’, 이 주문 하나를 처리한다, 실패하면 이 주문만 재시도, 로그도 이 주문 기준, 책임도 이 주문 기준


# In[ ]:


# named tuple

from collections import namedtuple

# 클래스 선언 - User 생성됨
# tuple 매직 메소드가 데이터 타입 바꾸듯, named tuple 도 데이터 구조 바꿈 - 행동 없음
User = namedtuple('User', ['name', 'country', 'job'])


# 객체 만들기
u1 = User(name = 'miji', country = 'Switzerland', job = 'ML engineer')


# 호출 - 일반 튜플과 다르게 딕셔너리처럼 key로도 접근 가능    

print(u1.name) 
# print(u1['name']) # 에러


# In[ ]:


# Dict로 받은 것을 named tuple 로

temp_dict = {'name': 'miji1', 
             'country': 'korea',
             'job': 'ds'}

u2 = User(**temp_dict) # 언패킹. (miji, korea, ds)를 name, country, job으로 나눠줌
# * 별 1개는 튜플 ** 별 2개는 딕셔너리
# 언패킹, 패킹 둘 다 가능

print(u2.name)
print(u1.name + u2.job)


# In[ ]:


# named tuple 메소드들

temp = [52,39, 100]

# _make(): 밸류 replace
u1 = User._make(temp)

print(u1)

# _fields : 필드 네임 확인

print(u1._fields, u2._fields)

# _asdict(): OrderedDict 딕셔너리 형태 반환

print(u1._asdict())


# In[ ]:


#  namedtuple로 객체 생성 data modelling 

Classes = namedtuple('Classes', ['rank', 'number'])
# student1 = Classes('A', 10) 같은 것을 4 클래스 * 20번까지 객체 생성 
        
strings = 'A B C'.split()
numbers = [str(n) for n in range (1,21)]

[Classes(s, n) for s in strings for n in numbers][0] # 이것들이 named tuple로 만들어진 각 row임. 동작 코드에 필요한 것. 이걸 가지고 다니다가 때가 되면 언패킹


# In[ ]:


# 데이터 타입

# 1. 컨테이너형: 서로 다른 자료형도 담을 수 있음 (e.g. list, tuple, collections.deque...)
# 2. 플랫형: 한개의 자료형만 담을 수 있음 (e.g. str, bytes, bytearray, array...) 플롯형만, 문자만

# a. 가변형: list, bytearray, array, deque
# b. 불변형: typle, str, bytes


# 무엇을 쓸 것인가? list vs. array
# 리스트: 컨테이너 타입이라 다양한 데이터 타입 다룰 수 있음 -> 유연, 범용적 사용
# 어레이: 숫자만 있을 때 빠르다. 리스트 기능과 거의 호환됨


# In[ ]:


# generator 

# 데이터가 너무 크거나, 한만번 쓰고 흘려보낼 경우 전부 메모리에 올리면 낭비 -> 한개씩 흘러나옴

# 만드는 법 1. list comprehension in tuple form

import array

chars = '+_()!@#$%^&*' # 불변형 + 플랫형

a = (ord(i) for i in chars if ord(i)>40) # 튜플형 + for루프
print(a)


# 만드는 법 2. 플로우로 쓰도록 함수로 만들 때 for loop + yield
# list(filter(lambda x: x>40, map(ord, chars)))
def func():
    for c in ['A', 'B', 'C', 'D']: 
        for n in range(1, 21): # 안쪽 for가 바깥 for로부터 아무것도 전달 안받아도 돌아감
            yield str(n)
            
# 제너레이터가 yield로 반환한 것은 이터레이터고, 이터레이터는 한번 소비되면 끝임. iter(str(n))
# 한번 출력되면 끝이므로 여러번 볼거면 제너레이터 결과물을 리스트에 담고 (리스트는 iteratable이라 여러번 출력 가능) 아니면 제너레이터 유지 


# In[ ]:


# tuple unpacking

print(divmod(*(100,9))) # (10,1)
print(divmod(100,9))
print(*(divmod(100,9)))

x,y, *rest = range(10)
print(x,y,rest)

x,y,*rest = range(2)
print(x,y, rest)


# mutable 가변 vs. immutable 불변

tupl = (15,10)
lis = [15,10]
print(id(tupl), id(lis))


tupl = tupl * 2
lis = lis * 2
print(id(tupl), id(lis)) 


tupl *= 2
lis *=2
print(id(tupl), id(lis)) # *= 2 는 *2와 내부 연산 다름. *=는 객체 새로 안만들고 기존 객체값을 업데이트 해서 ID 안바뀜 (648 ->648)
                        # *2 는 객체 새로 만들어서 객체 ID다름 (944 -> 648)
                        
                        # 튜플은 수정이 불가능하므로 바뀔 때마다 새 객체가 생기지만 (id 다름. 880 -> )
                        # 리스트는 수정 가능해서 기존 객체 유지됨 (id 같음. 648)


# In[ ]:


# sort vs. sorted

# sorted: 정렬 후 새로운 객체 만듦

f_list = ['strawberry','apple', 'papaya']

print('sorted - ', sorted(f_list), 'original-', f_list) # ascending. 원본 그대로
print(sorted(f_list, reverse =True)) # descending
print(sorted(f_list, key = len)) # 단어 길이순
print(sorted(f_list, key = lambda x: x[-1])) # key에 내가 만든 함수 넣음. 마지막 알파벳순

# sort: 정렬 후 원래 객체 변경
# 반환 값 확인하면 None 나옴

print('sorted - ', f_list.sort(), 'original-',f_list)   # 원본 수정됨
                                                        # 반환 값 확인하면 None 나옴 - 원본을 바꿨기 때문에.
                    # 원본을 바꾸는 메서드 (append, update, extend, reverse, add)는 값을 사용하라고 만든게 아니어서 print시 출력 없음


# In[ ]:


# hash table : key에 value를 저장하는 구조

my_dict = {"apple": 5, "banana": 10}

# 모든 불변 데이터에 (str, int, tuple...) 해시값 이라는 것을 만들고 할당해 수많은 데이터 중 특정 데이터를 즉시 찾을 수 있음
# hash table은 Dict처럼 key, value 함께 저장. key는 str (불변값)이므로 각 키마다 해시값 존재
# print(hash('apple')) -368284358071110661 가 apple의 해시값. 해시값에 따라 특정 위치 (index) 결정되고 key, value함께 보관

# .get('apple') -> apple의 해시값 계산 -> 3684.. 위치로 가서 해시값 맞나 비교 -> value 꺼내줌 의 플로우.
# 유저 많은 네이버에서 ID 치면 비밀번호 즉시 매치되서 로그인 되는 것도 동일 원리
# dict뿐만 아니라 set도 해시 테이블로 만들어져 인덱스에 직접 접근해서 값 존재 여부 빠르게 리턴

# 해시 key는 검색 수단이므로 수정 불가능 & 중복 불가능. (value는 수정, 중복 가능) -> 수정, 중복 가능한 list는 해시값 생성 불가능.
# 따라서 수정 불가능, 중복 불가능한 dict, set만 해시 구조로 만들어짐
  

print(hash('apple'))

t1 = (10,20,(10,20))

print(hash(t1))


# In[ ]:


# tuple 을 dict 로 변환하기 - 특히 중복된 key가 있을 때 

source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict = {}

# 방법 1 - no use Setdefault

for key, value in source:
    if key in new_dict: # 해당 key가 이미 삽입되어 있을 경우 - 중복 key
        new_dict[key].append(value)
    else: # 해당 key가 처음 들어가는 경우
        new_dict[key] = [value]
print(new_dict)


# 방법 2 - Setdefault

new_dict = {}

for key, value in source:
    new_dict.setdefault(key, []).append(value)
print(new_dict)


# 주의

new_dict = {key: value for key,value in source}
print(new_dict) # 중복된 키가 있을 경우 차곡차곡 넣지 않고 마지막 값으로 리뉴얼 되버림


# In[ ]:


# immutable Dict

from types import MappingProxyType

d = {'key1': 'value1'}
d_frozen = MappingProxyType(d) 

d['key2'] = 'value2' # 수정 가능
# d_frozen['key2'] = 'value2' # 수정 불가능


# In[ ]:


# 집합

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s4 = set() # 빈 집합. {}은 빈 Dict이 되니 주의
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}) # 읽기 전용으로

s1.add('Melon')
s1 # 중복값 빠지고 melon 추가됨
# s5.add('Melon') # 추가 불가. 에러남


# 선언 최적화

from dis import dis
print(dis('{10}')) # {10}으로 집합 선언시 3단계만 거침 
print(dis('set([10])')) # list 거쳐서 집합 선언 시 6단계 거침 


# In[ ]:


# 일급 함수
# 아래 조건을 만족하면 일급 객체. 함수가 만족해서 (=함수를 값처럼 자유롭게 다룰 수 있어서) 함수는 일급 객체 -> 함수형 프로그래밍을 가능하게 함


# 특징 1. 변수에 담을 수 있다

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)   # 재귀함수. 함수 내에서 함수를 호출

var_func = factorial
print(var_func(5)) # factorial 을 var_func에 넣을 수 있고, 실행도 가능 
print(list(map(var_func, range(1,5))))

# 특징 2. 함수를 인자로 전달 가능
# 특징 3. 함수로 결과값 반환 가능

print([var_func(i) for i in range(1,5) if i%2]) # var_func를 리턴값으로 받음 
print(list(map(var_func, range(1,5)))) # var_func 를 인자로 전달


# In[ ]:


# 함수형 프로그래밍: 지금은 계산 방법만 조합하고/ 계산을 나중으로 미루고 필요할 때 실행
# 팩토리얼처럼 중간 결과는 함수 안에 저장돼있다가 호출 or 리턴되면서 안에서부터 하나씩 계산됨
# 이게 가능하려면 함수가 일급 객체여야 함 (함수를 인자로 전달하고, 함수를 결과값으로 받을 수 있음)

# 장점
# 1. 데이터 간단 변환 및 전처리 쉬움 : list(map(lambda x: x+1, ages))
# 2. 순차적인 여러 단계를 라인 하나에 줄줄이 연결하기 좋음 : 데이터 받아서 → 조금씩 바꿔서 → 다음 단계로 넘기는 데이터 파이프라인에 강함


# In[ ]:


# 참고 - map, filter, reduce : 함수를 인자로 받는 대표적인 메소드들
# 함수가 일급 객체라서 이걸 가능하게 함

print(list(map(var_func, filter(lambda x: x%2, range(1,6))))) # 익명함수 lambda x를 filter함수의 인자로 전달
                                                        # var_func도 동일하게 map함수의 인자로 전달
                # 함수 lambda x:x%2는 아직 실행 안됐음. var_func 호출되면 기다렸다가 그때 계산될 것
                                                        
from functools import reduce

reduce(lambda acc, x: acc + x, [1,2,3,4]) # add함수를 인자로 받음
                            # reduce: 값의 갯수가 줄면서 이전 값에 누적시켜 하나만 남김


# callable : 메소드 형태로 호출 가능한지 확인

print(callable(str), callable(list), callable(3.14))
# 3.14(234) 이런 식으로 호출이 불가능하므로 


# In[ ]:


from functools import partial

five = partial(var_func, 5)
five()


# In[ ]:


# prtial 사용법: 인수 고정해 콜백 함수로 사용. 고정해 놓았으니 호출만 하면 됨
# 콜백 함수: 지금 당장 실행하지 않고, 나중에 필요할 때 호출해 주기로 맡겨둔 함수

from operator import mul
from functools import partial

five = partial(mul, 5) # 인수 5 고정
print(five(10))

func_five = partial(var_func, 5) # 함수를 var_Func로. 인자 1개만 필요한데 5는 이미 고정
print(func_five())

six = partial(five, 6) # 인수 추가 6 고정
print(six())

print([five(i) for i in range(1,10)]) # five함수가 return 값으로 쓰임
                                    # 5는 고정되고 5*1, 5*2, ..., 5*10
print(list(map(five, range(1,10))))


# In[ ]:


def outer():
    emp = []
    def inner(value):
        emp.append(value)
        print(emp)
        return sum(emp)/len(emp)
    return inner

f = outer()
f(10)
f(20)


# In[ ]:


# 클로저 : 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장. 이후 접근 가능

# 외부함수 outer 실행시 만들어지는 지역함수 inner 와 지역 변수 x=10는 공유하지만, 변경 불가능 (immutable)
# 불변 자료구조 -> 멀티스레드 (코루틴) 프로그램에 강점


# 예시 1 

def outer():
    
    # 클로저 영역
    x = 10 # free variable
    def inner():
        return x
    return inner # 함수가 일급 객체기에 inner 함수를 return에 넣을 수 있음

f = outer()  # f는 inner 함수 자체일뿐 (아직 실행x). inner 실행하려면 객체에 () 추가.
print(f())   # f() == inner()


# outer가 실행되면 outer 에 직접 속한 x가 사라져야되는데 하필 inner객체가 리턴되고, 그 inner객체가 붙잡고있는 바람에 덩달아 x=10이 살아있음.
# f같은 새 변수에 할당되어도 x=10은 여전히 살아있음.
# 클로저 되려면 중첩 함수 + 외부 지역 변수 참조가 꼭 필요


# In[ ]:


# 예시 2

def outer():
    series = [] 
    
    def inner(value):
        series.append(value)
        print(series)
        return sum(series)/len(series)
    return inner  

closure = outer()  
print(closure(10))   # series를 복사 후 저장해놔서 계속 접근하면서 누적시킬 수 있음. 값 보존 되있기때문에

    # inner 아래 emp에 10을 추가하려면 def inner (value)라고 인자 받을 자리를 만들어줘야 
print(closure(20))


# In[ ]:


# 증명

print(closure.__code__.co_freevars) # closure가 상태 저장하는 co_freevar 자유변수인 series를 가지고 있음 

print(closure.__closure__[0].cell_contents) # 자유변수 안에 값이 다 저장되어 있음


# In[ ]:


# 주의: 외부 변수 수정 시 클로저 사용

def outer():
    cnt = 0
    total = 0
    def inner(v):
        nonlocal cnt, total
        cnt += 1 
        total += v
        return total / cnt
    return inner

closure = outer()
print(closure(10))  # nonlocal 없이 돌리면 지역 변수 정의된게 없다고 에러

# closure는 read-only라서, 외부 변수가 새로운 객체를 가리킬 수 없음. 다만 append로 내부 상태를 바꿀수는 있음
# total = total+1은 total+1이라는 완전 다른 숫자 (= 새로운 객체)를 total이라고 부르게 이름만 바꿈 -> 객체 자체가 바뀜
# -> 클로저에 외부 변수 객체 자체를 바꾸는 옵션은 없기에 지역 변수가 없다고 에러난 것. 
# emp.append(v)는 emp라는 객체가 안바뀜. 업데이트만 됐을 뿐.

# 디버깅 편의를 위해 중첩 함수에서 외부 변수 이름 쉽게 못바꾸는게 파이썬 설계 룰. 
# 의도적일 때만 외부 변수를 nonlocal로 명시


# In[ ]:


# closure의 클래스 버전 - 변수가 많다면 이쪽이 더 유리

class Averager():
    def __init__(self):
        self._series = []
        self._variable1 = 0
        self._variable2 = 0
        
    def __call__(self, v):
        self._series.append(v)
        return sum(self._series)/len(self._series)
        
averager_cls = Averager()

print(averager_cls(10))
print(averager_cls(20))


# In[ ]:





# In[ ]:


# 데코레이터 : 같은 기능의 함수를 여러 함수에 고치지 않고 붙여 중복 코드 없이 새 함수 반환
# 클로저와 형태 거의 유사 - 바깥 함수를 실행해야만 안의 함수를 리턴 받음


# 공통 행동 부분 : 
 
def outer(func):
    def inner(*args):   # *args : 들어오는 변수 갯수에 제약 없이 모두 언패킹 할 수 있도록
        result = func(*args)  # func 는 외부 변수 - inner가 자기 안에서 정의되지 않은 변수를 쓰고 있으므로 클로저
                            # args로 인수 몇개가 들어오더라도 func() 실행되면서 '내부' 슬롯에 나뉘어서 할당됨 (언패킹) result에 할당되는게 아님
        name = func.__name__ 
        arg_str = ', '.join(repr(arg) for arg in args) # 제너레이터 형식
        msg = f"func_name: {name}, arg_str: [{arg_str}], results: {result}"
        return msg # return print() == None 
    return inner


# outer 없이 def inner: return msg로 써도 돌아가긴 함. 그러면 데코레이터의 핵심 (함수 교체, 클로저, 재사용)모두 잃음
# 추가



# 개별 행동 부분

@outer  # 데코레이터 사용 위해 붙임 
        # 개별 코드 위를 공통 행동으로 장식해줌 -> decorator 
def avg_func(*num): # avg_func(10,20,30) 처럼 불러질 떄 튜플이 아니고 세개의 위치 인자를 넘긴 것.
                # num 변수 하나로 묶은 뒤 inner 
    return len(num)

@outer  
def sum_func(*num):
    return sum(num)

# outer 실행되면 inner 객체가 실행되는데, 그게 func를 참조하므로 func가 저장되 있음
# @outer 먼저 실행되고, inner 객체 만들면, avg_func가 func 대체해, 최종 리턴값 msg 
# avg_func와 sum_func가 코드 수정 없이 똑같은 outer 행동을 하도록


# In[ ]:


# 만약 데코레이터 없었으면 공통 행동 부분에서 중복 많았을 것 (아래 참조) 

# def avg_func(num):
    # def outer (avg_func):
        # def inner (arg):
            # result = avg_func(arg)
            # name = 
            # arg_str = 
            # msg = 

# def sum_func(num):
    # def outer (sum_func):
        # def inner (arg):
            # result = sum_func(arg)
            # name = 
            # arg_str = 
            # msg = 


# In[ ]:


# 데코레이터 사용

print(avg_func(100,200)) # 부를 때는 원래 함수로 바로 실행 가능
print(sum_func(100,200,300,400,500))


# In[ ]:


# 데코레이터 미사용

# 데코레이터 안쓰면 바깥 함수 불러서 나온 내부 함수 객체를 다른 이름에 어사인하고 다시 불러야 함 -> 번거로움
# 데코레이터 쓰면 원래 함수만 부르면 되니 간단

wo_deco1 = outer(avg_func) 
wo_deco2 = outer(sum_func)

print(wo_deco1, ", free var: ", wo_deco1.__code__.co_freevars) # wo_deco는 이미 클로저. 자유변수로 함수를 참조중. 
                                                                # 데코레이터만 아닐 뿐임
print(wo_deco2, ", free var: ",wo_deco2.__code__.co_freevars)

wo_deco1(100,150,200)
wo_deco2(100,200,300,400,500)


# In[ ]:


# Concurrency

# 반복 가능 타입(iterable): collections, string, list, dict, set, tuple, unpacking, *args, ... 
# generator가 하나씩 꺼내줘서 iterator를 만들어서 반복 가능하게 해줌

t = 'ABC'
w = iter(t) 
# 모든 iterable은 __iter__매직 메소드 가져서 iter(x) 호출하면 iterator 객체 생성
# -> 이터레이터는 반드시 __next__가지므로 next(x) 호출


print(next(w))
print(next(w))
print(next(w))
# print(next(w)) # 더 없으면 stop iteration

 # 지금까지 어떤 것이 호출되었는지 위치 정보 기억 -> 다음에 뭘 호출할지 안다 (이터레이터라서)


# In[ ]:


# 같은 것을 
# while

t = 'ABC'
w = iter(t) # 이전 블록의 w가 iter(). 이터레이터는 next()로 한 번 출력되면 끝이므로 다시 정의

while True:
    try:
        print(next(w))
    except StopIteration:
        break


# In[ ]:


# next 패턴

class WordSplit:
    index = 0

    def __init__(self, text):
        self._text = text.split(" ") 
    
    def __next__(self):
        try: 
            word = self._text[self.index] # index가 범위를 벗어나면
        except IndexError:
            raise StopIteration("Stop Iterating.") # index error 생기면 stop iteration을 대신 던져라
        WordSplit.index += 1
        return word

wrd = WordSplit("Hello World Python")

print(next(wrd))   # 클래스지만 iterable
print(next(wrd))   
print(next(wrd))   
# print(next(wrd))     


# In[ ]:


# generator 패턴

class WordSplit:
    def __init__(self, text): 
        self._text = text.split(' ')
        
    def __iter__(self):
        for word in self._text:
            yield word      # yield로 제너레이터로 바뀌어서, __iter__에 __next__를 자동으로 구현해줌 (=제너레이터)
                            # 그 덕분에 다음 def __next__안깔아도 next(wt) 먹힘

wrd = WordSplit("Hello World Python")

wt = iter(wrd) # 이터레이터 객체
# print(dir(iter(wrd)))

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))


# iteratable은 도서 앱에서 돌아가게 확장자가 바뀌는 (__iter__) 기능 갖춘 책 파일 (list, tuple, range, set)
# -> 앱에 넣었음 : iter(책 파일)
# iterator는 도서 앱에서 돌아가고 있는 책. 페이지 넘길 수 있음 (+__next__) 앱에 일시 중단된 위치 저장되있음
# +next() 누르면 책 넘어감. 

# 사람이 직접 클래스로 설정하는 이터레이터는 __iter__ 와  __next__를 원래 모두 갖춤. 안그러면 에러남
# 그중 __next__는 사람이 수동으로 구현해서 next(x) 먹히게 헤야 함. (예외 - iter(x)처럼 파이썬이 이터레이터 객체 만드는 경우 파이썬이 자동으로 __next__깔아놨음)
# 근데 제너레이터는 __iter__상태에서도 __next__사람이 구현할 필요 없이 __next__ 쓸 수 있게 해줌. 
# 하지만 다음 값으로 부르는건 for루프, next()등 외부 압력이 필요


# In[37]:


# 병행성 (concurrency): 단일 프로그램 안에서 여러 작업 동시에 수행(하는 것 같아 보임)
# 각 작업에서 한 줄씩만 번갈아 실행. 이번 블록 실행하다가 잠깐 멈춰놓고 다른 블록 실행하다가 돌아옴.   
# 제너레이터 덕분에 실행 중간에 멈춰 + 어디까지 했는지 기억 (클로저)+ 하던 작업 어떻게 해왔는지 기억 

# 병렬성 (parallelism): 여러 컴퓨터가 여러 일을 동시에 수행


# 제너레이터 

def gen_func():
    print('Start')
    yield 'A Point' # yield 두가지 역할: 1. 그 지점에 "닿을 떄까지" 코드를 실행한 뒤 멈추고 위치 저장하는 체크 포인트
                                    # 2. yield 값을 호출자에게 전달하는 역할
    
    print('Continue')
    yield 'B point'
    
    print('end') # return이 하나라도 있으면 제너레이터
    # yield 'C point'
    
temp = iter(gen_func()) # 제너레이터니까 __iter__ 가능 -> 반복 가능해짐

print(next(temp)) # 제너레이터 gen_func에 __next__ 자동 갖춰졌으니 가능
            # 잠깐 멈춰있음. (여기서 다음 블록으로 갈 수 있음) 어디서 중단됐는지 기억중
print() 

print(next(temp)) # 'A point'에서 중단됐단거 아니까 다음부터 바로 시작할 수 있음
print()

print(next(temp)) # 암묵적인 return으로 끝났기에 stop iteration
# print(next(temp))


# In[ ]:


# 제너레이터를 부르는 방법 차이
# 방법 1 : for loop
 
temp2 = (x*2 for x in gen_func()) # 제너레이터 객체 get_func()는 이터레이터면서 이터러블

for i in temp2:
    print(i) # 한 yield 단계씩 나오고 쉬었다가 다시 나옴
    

# 제너레이터 gen_func 한번 쓰면 사라지는데 왜 temp2, temp3 에서 여러번 부를 수 있음?
# 제너레이터 함수는 무한히 사용 가능. def gen_func()는 아직 설계도 상태라서 무한히 찍어낼 수 있음
# 제너레이터 객체 temp는 한번만 사용 가능 (for문 돌릴 때마다 temp 재활용 말고 새로 gen_func()로 돌려주면 함수를 매번 새로 실행시키는거니까 다시 쓸 수 있음)


# In[ ]:


# for loop에서는 stop iteration error가 나지 않음.

# for 문이 StopIteration을 내부에서 잡아먹기 때문에 try StopIteration: except를 쓸 필요가 없다.
# stop iteration은 내가 next(g)로 직접 불렀기 때문에 난 것


# In[ ]:


# 방법 2
# list

temp3 = (x*2 for x in gen_func())
print(list(temp3))

# list()는 yield/return 호출물을 append 하는거니까 
# next() → print('Start')→ yield 'Point A'→ append
# next() → print('Continue') → yield 'Point B' → append
# StopIteration 인데 print는 어펜드 될 수 없으니 따로 나오고 yield로 전달된 것들만 리스트에 모인 것. 동시 실행된 것


# In[ ]:


# 제너레이터의 return

# 리턴은 코드 종료 선언-> stop iteration 던짐
# yield는 next()통해 밖으로 값을 전달하지만 return은 그냥 끝을 선언하는 것

def gen():
    yield 1
    return 42

g = gen()
print(next(g))   # 1
print(next(g))   # StopIteration(42)
# 42는 next()의 반환값이 아님

# 코루틴 간 통신용으로 return 존재


# In[ ]:


# 제너레이터 부수 효과: 함수가 값을 “빼주는 것”(yield) 말고, 숨은 영향을 만드는 것

# 1. print

def gen_func():
    print('Start') # -> 글자만 출력되고 어디에도 저장 안됨
    yield 'A Point'
    
# 2. append

results = []

def gen():
    for i in range(3):
        results.append(i)   # 외부 리스트 results가 몰래 바뀜 (몰래 바뀜)
        yield i # 값 담으려면 append 말고 list(gen())으로 담기


# In[ ]:


import itertools

gen = itertools.chain('ABCDE', range(1,11,2))
print(list(gen))

# itertools없었다면, 숫자 연산값을 반환하는 제너레이터 필요할때마다 인간이 def func(): yield from 안에서 계산식 하나하나 코딩해야.
# 인간을 편리하게 + 코딩 에러 위험 제거 하는 라이브러리
# itertools.chain('ABC', range(3))는 이터레이터를 만듦. def func(): yield from 추가 결합할 경우 gen()이 제너레이터 객체 됨. 제너레이터가 가진 __next__ 덕에 밖에서 next(g)를 눌러주면 값이 하나씩 나온다

# iterable / iterator-> (itertools 활용해서) -> generator -> for loop / next()


# In[ ]:


# count

gen1 = itertools.count(1, 2.5) # 1에서 2.5씩 무한으로 더함
print(next(gen1))
print(next(gen1))
print()


# takewhile: iterable 에서 람다 함수 만족하는 값만 선택해 이터레이터로 바꿔줌
# filter의 이터레이터 버전
#  itertools.takewhile(함수, iterable)

gen2 = itertools.takewhile(lambda x: x<10, itertools.count(1, 2.5)) # count와 같이 쓰일 때 특별히 while 문 역할
print(next(gen2))
print(next(gen2))


for i in gen2:
    print(i)


# In[ ]:


# filterfalse - 람다 조건이 안맞는 것만 반환
# takewhile (filter) 의 반대

gen3 = itertools.filterfalse(lambda x:x<3, [1,2,3,4,5])

for i in gen3:
    print(i)
print()
    
# 누적 합계

gen3 = itertools.accumulate([x for x in range(0,5)])
print(list(gen3))
print()


# 연결

gen5 = itertools.chain('ABC', range(0,11,2)) # 콤마 앞과 콤마 뒤를 이어서 한 리스트로
print(list(gen5))

gen6 = itertools.chain(enumerate('ABC'))
for i in gen6:
    print(i)
print()


# cartesian product - 원소 조합별 경우의 수

gen7 =  itertools.product('ABC') # repeat = 1일때는 개별로 쪼개기
for i in gen7:
    print(i) # 개별 튜플로 뽑음
print()

gen7 =  itertools.product('ABC', repeat = 2)
print(list(gen7))


# 그룹화 SQL groupby

gen8 = itertools.groupby('AABBC')
# print(list)

for str, group in gen8:
    print(str, list(group))


# In[ ]:


# 코루틴 coroutine
# 실행 흐름을 양방향으로 (send(), yield 로) 주고받는 함수
# def,yield를 사용하니 제너레이터와 같아 보이지만 뜻은 완전 달라 헷갈림 (제너레이터는 일방향, 코루틴은 양방향)-> 요즘 async, await로 바뀜


def cor1():    # sub routine
    # 제너레이터, 코루틴, 함수 모두 def로 선언됨. def라고 무조건 함수라고 생각하지 말고 내용 확인
    print("start")
    i = yield
    # print(i)
    print("received: {}".format(i))
    

cr1 = cor1() # # main routine - 제너레이터 선언
next(cr1) # yield까지 수행. i 변수에 받은 것도 없고 i 자체만으로는 아무것도 안나오니 (print(i) 아니고)start만 나옴. 
            #  yield 지점까지 서브루틴 수행
# next(cr1) #  기본 전달값 None


# 값 전송 

cr1.send(100) # send가 next기능도 포함하고 있음? i=yield에 멈춰있다가 메인 루틴에서 100 넘기면 서브 yield에서 받아서 i에 할당하고 다음 yield까지 전진. 없으니 그냥 끝 



# In[201]:


# 잘못된 사용

def worker(name):
    while True:
        task = yield
        print(f"{name} 처리:", task)

wo = worker("A") # 제너레이터 객체만 생성됨. 아직 함수까지는 안돌아간 상태 
# next(wo) # 함수 while True 시동 건 다음 첫번째 yield까지 쭉 실행해야
            # 일단 next()로 수신기가 있는 yield 까지는 가줘야만 값을 보낼 (혹은 받을) 수 있음

wo.send(1)


# In[ ]:


# yield 문법 1 : result = yield something

#  yield 다음의 something이 변수 result로 들어가지 않음. 보통은 밖으로 내보내기만 함
#  result에 들어가는 것은 send()로 값 넣었을때만 예외.
 
def gen():
    x = yield 1
    print("x =", x)

g = gen()
print(next(g))  # 1이 x에 들어간게 아니라 yield 1이므로. x는 아직 none
g.send(10)  # x =10 대입됨. 하지만 여전히 yield에 들어간건 아님.
        # send가 next()역할도 해서 더 나아가려는데 이제 없으니 stop iteration


# In[184]:


# yield 문법 2 - yield from : yield from <iterable>


# 내부 제너레이터(또는 이터러블)의 모든 yield가 외부로 "흘려보내짐:
# sub()에서 받은 yield는 main()에서 여전히 밖으로만 나감 - 리스트, 튜플식으로 받아서 사용 가능 형태로
# 원래 yield 문법상 죄측 변수에 할당되지 않는 것 동일


def gen():
    yield from 'AB'
    yield from range(1,4)
    
t = gen()
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))

print()



# 중첩 코루틴 깔끔하게 처리에 좋음
# 동일 결과

def gen1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y
        
t1 = gen1()

for v in t1:
    print(v)


# In[ ]:


# 특수한 경우: yield from 에 return 이 처리되는 방식 

# sub()의 return은 main()에서 result 변수에 전달. 흘려보내지 못하고 "담겨짐"
# return은 yield로 만들어진 값이 아니기 때문에 흘려보내지지 못해, 출력값이 정상적으로 왼쪽 result 변수에 담김
# return은 yield from 제너레이터 작업의 "최종 결과값"으로 전달됨

def sub():
    yield 1
    yield 2
    return "done"

def main():
    result = yield from sub()
    print(result)

g = main()

list(g) # [1,2]
# list로 묶으면 흘러나온 yield만 수집되므로 [1,2]만 나옴
# done은 result가 받아서 print(result)때문에 나옴


# In[ ]:


# 중첩 제너레이터 (for 문)에서는 send()가 보내지지 않음-> yield from으로 변경

def subgen():
    x = yield 1
    print("subgen got:", x)
    y = yield 2

def main():
    for v in subgen():
        yield v

m = main()

next(m)
m.send(3)
# print(next(m))
# print(next(m))

# main()에서 나오는 값은 for루프에서 값만 추출될 뿐 ->
# main()으로 보낸 send()는 subgen()까지 전달이 안됨

# 바뀐 버전

def subgen():
    x = yield 1
    print("subgen got:", x)
    y = yield 2
    
def main():
    yield from subgen()


# In[ ]:


# getgeneratorstate

# GEN_CREATED: 처음 대기 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPEND: yield 대기 상태 - 이때 send로 값 보내거나 받을 수 있음
# GEN_CLOSED: 코루틴 실행 완료 상태

# yield를 기준으로 오른쪽은 밖으로 흘리는 값, 왼쪽은 입력을 받은 값

def cor(x):
    print("start: {}".format(x))
    y = yield x 
    print('received: {}'.format(y))
    z = yield x+y
    print('received again: {}'.format(z))


cr = cor(10)

from inspect import getgeneratorstate # 코루틴 상태 확인

print(getgeneratorstate(cr))

next(cr) # x에 10 넣고 시작. yield 위치까지 실행됨 (10 내보내짐)
        # y 받을 준비 완료 (yield x는 이미 값 정해져서 흘렸으니 같은 줄의 y 차례)

print(getgeneratorstate(cr))
cr.send(10) # yield는 값 내보내기+ 멈춘 자리에서 외부 값을 받는 지점
            # y로 값 보낼 준비 됐는데 next()로 패스하면 어쨌든 None 넘겨짐

print(getgeneratorstate(cr))
cr.send(100) # z로 보냄


# In[ ]:


# 구현 목표

# 동시성 concurrency: 요리하는 사람 1명이 혼자 밥 짓고 국 끓이고 반찬 만든다 -
# 한번에 한 행동만 하지만 / 밥,국,반찬은 동시에 진행중

# 병렬성 parellelism: 같은 순간에 복수 태스크가 진행됨
# 주부 3명이 각자 밥, 국, 반찬 맡아서 요리



# 동시성 구현 방법 (요청 함수가 결과를 들고 돌아오나? 나중에/다른 통로로 결과가 도착)
# - 동기: A 요청하면 결과 받기 전까지 (=끝날 때까지) B 실행 x. 카페에서 커피 요청하면 그 자리에서 커피 받고 돌아와야 함
# 다음 행동은 이전 커피 요청의 결과를 받은 후에야 가능 -> 완료까지 내 일 못하는 건 (blocking) 부수적인 과정
# 어원 - A의 일정은 B 일정에 종속돼있다. 맞춰져있다 =동기화

# - 비동기: A 요청하면 결과를 들고 돌아오지 않는 것. 카페에서 커피 요청하면 일단은 빈 손으로 돌아옴.
# A 걸어놓고 기다리는 동안 B로 제어권 넘어가서 다른 일함. 카톡 보낸 뒤 (요쳥) 나는 바로 답 못받고 (결과는 나중에 옴), 답 오면 확인. 
# -> 스레드 1은 스탠바이 상태로 대기 시키고, 내 실행 흐름에서 빠져서 스레드 2의 다른 일 (non-blocking)은 부수적인 과정 
# 어원 - A의 일정은 B와 분리. 안맞춰져있다

# 비동기를 통해서 동시성 구현 가능


# In[ ]:


# blocking 여부 (요청 결과 기다리는 동안 다른 일 할 수 있나? = 호출시 제어권 있는가)
# - blocking: 기다리는 동안 실행 흐름 멈춤. 결과 받을 떼까지 그 스레드/코루틴은 아무것도 못함
        # - blocking I/O: 기다리는 값 올때까지 디른 작업 못함. 데이터 요청 보내면 제대로 된 데이터 올때까지 멈춤
        #       스레드 1이 계산중/ 스레드 2가 I/O 중이면 스레드 2가 I/O 블로킹 됨. 
                # 스레드 1이 제어권 (무슨 코드를 돌릴지 결정할 권한)을 갖고, 스레드 2는 제어권을 잃음
#       - blocking CPU: 계산 끝날 때까지 멈춤. 스레드 1이 계산중/ 스레드 2가 대기중 runnable이면 스레드 2가 CPU 블로킹 됨
                # 스레드 1이 제어권 유지
# - non_blocking: 기다리는 동안 멈추지 않음. 
        # - non blocking I/O: 데이터 요청 보내면 일단 접수 완료증 (Future - 아직 존재하지 않는 결과를 나중에 채우기 위한 객체) 바로 받는 것에 만족하고 돌아가서 다른 일. 다음에 제대로 된 데이터 받음
        # 호출한 스레드/코루틴이 즉시 반환되므로 (Futures 반환) 대기 상태로 멈추지 않음 = IO가 제어권 잃지 않음


# blocking/non-blocking != 동기/비동기
# 비동기 + 블로킹: 커피 주문하고 자리 뜬 뒤 (비동기) + 멍하니 기다림 (블로킹)
# 비동기 + 논블로킹: 커피 주문하고 자리 뜬 뒤 (비동기) + 내 노트북 작업 함 (논 블로킹)
# 동기 + 블로킹: 커피 주문하고 그 자리에 서있으면서 (동기) 암것도 안하고 기다림 (블로킹)
# 동기 + 논블로킹: 커피 주문하고 그 자리에 서있으면서 (동기) + 내 노트북 작업 함 (논 블로킹)


# 동기/비동기: 결과를 언제, 얼마나 빨리 받나
# blocking / non-blocking: 기다리며 멈추나


# In[ ]:


# 프로세스: 한 컴퓨터에는 동시에 여러 프로세스가 돌아감. 프로그램 (크롬, VSCode...)도 각각 프로그램. 
# 같은 프로그램 내에서도 여러 프로세스를 띄움 

# 멀티 프로세싱 - 크롬 브라우저가 탭마다 별도의 프로세스 띄워서 한 탭 죽어도 다른 탭 살아있음
# 한 파이썬 스크립트 내에서도 여러 자식 프로세스 띄움 
# 특징: 메모리 분리 -> 무겁지만 안정적


# 스레드: 한 프로그램 내에서 일하는 작업 단위
# 크롬 프로세스안에서 GPU 스레드 (그래픽/동영상 재생), Main/UI 스레드 (화면 로딩, 주소창 입력 처리, 클릭 이벤트) 등 여러 스레드가 서로 다른 일함

# 멀티 스레드 - 크롬 내 여러 스레드가 각자 동시에 일하는 것
# 특징: 컨텍스트 전환 비용 낮음 -> 빠름. 메모리 공유 -> 하나 터지면 같이 영향 받음

# 단일 스레드: asyncio 와 함께 사용하면 CPU-> I/O대기 변경을 스레드 하나에서 코루틴 바꿔가면서 번갈아 할 수 있음. async쓰면 단일 스레드에서도 non-blocking I/O 처리 가능해서 효율적 사용 가능
# 기다렸다 늦게 일 처리하는건 멀티 스레드와 같지만, 멀티 스레드는 여러 I/O bound를 겹쳐둘 수 있어 이점 (=CPU 공백 없앰). 많은 I/O 작업이 (DB 조회, 네트워크 대기, 파일 읽기..) 동시에 '실행'되는 것이 중요
# 멀티 스레드는 I/O 바운드 대기 끝난 뒤 기다리던 태스크들이 ‘task을 CPU까지 올리는 흐름'이 여러 스레드에 분산되서 빠르게 할당/처리 (task 처리는 GIL 제한 없음) -> task 밑작업으로 CPU가 잘 준비됨


# In[ ]:


# I/O bound : 기다리는 시간이 길어서 코드가 느리다. "이벤트" 발생으로 인해 (e.g. 기다리던 데이터가 도착하거나) ㅇ 끝나면 queue 에서 기다리던 일 몰려서 병목 생김.
#                                     -> I/O bound 코드는 (=대기 많은 작업) 멀티 스레딩 사용. I/O 스레드는 GIL 놓으니 CPU 하나 들어오면 GIL 소유권 바로 잡을 수 있어서
#                                     -> I/O bound는 단일 스레딩이 느리다. 그냥 기다릴 수밖에 없어서 (async 안쓰는 경우 한정. async 쓰면 쉬는 시간에 다른 가벼운 CPU 작업을 박아넣을 것)
# CPU bound : 계산이 많아서 코드가 느리다 -> CPU bound 코드는 (=무거운 작업) 멀티 프로세싱 사용. GIL 제약을 우회할 수 있어서.
#                                     -> CPU bound 작업은 멀티 스레드가 느리다. GIL이 병목 (=GIL 때문에 느림)이라
                                        # 컨텍스트 스위칭 때문. 스레드1: Python 계산 (GIL 점유중) 스레드2: Python 계산 대기중 일 때 OS는 스레드를 바꾸려고 시도함.
                                        # 하지만 스레드2는 GIL 없어서 실행 못하고 인터프리터는 다시 스레드 1로 돌아감. 
                                        # 결과: 일은 스레드 1만 진행되는데 스위칭만 계속 발생하므로 시간 낭비됨.




# 참고) 한 스레드 계산 다 끝날 때까지 OS 스캐줄러는 기다려주지 않음.
# 스레드는 CPU를 타임 슬라이스 (CPU를 한 스레드/ 프로세스에게 빌려주는 시간 조각) 동안 쓸 수 있고, 
# 시간 다 되면 OS 스케줄러는 CPU를 다음 스레드로 넘기는 시도.
# 하지만 GIT은 누가 파이썬 코드를 돌릴지 파이썬 인터프레터에 의해 결정되고, 인터프레터와 스케줄러는 다른 조직임.
# 새 스레드가 CPU를 가졌어도 파이썬 코드는 전혀 못돌리니 (block 상태. GIL 대기) 바로 다시 원래 스레드로 돌아가거나 잠시 대기하다 밀려남
# OS가 넘길 때 끝났는지 안중요하고 시간 다됐는지만 중요

# 하지만 GIL은 주기적으로 or I/O 진입 시도 시 반납된다
# OS가 이미 다른 스레드로 전환해서 실행중이면 그 스레드가 GIL 획득 & 바로 계산 -> OS 스케줄링은 GIL handoff 준비하는 역할


# In[ ]:


# GIL : 한 프로세스 내 하나의 스레드만 CPU 작업을 할 수 있음. 나머지 스레드는 I/O 기다림. 한 프로세스 내 모든 스레드의 행동을 간접적으로 규제.
# - 소유권 개념. CPU 작업중인 스레드 1이 GIL을 잡고 있음. I/O 대기중인 스레드 2에 작업 가능 알람이 오면 GIL 소유권 가짐. 스레드 1은 소유권 놓음


# In[ ]:


# futures + map (시간 제한 없이 기다려줌)

# 잠깐 . 뭘 먼저 시작하느냐는 완전히 랜덤인거야? 그리고 만약 list[0] 의 스레드 1이 먼저 시작됐다고 해보자. 그럼 스레드 1 끝날떄까지 스레드 2,3은 대기 상태지? 그리고 스레드 1 끝나면 GIL이 2,3중 하나로 넘어가면서 다음이 시작되는거고

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed  
# futures: 비동기 실행 위한 API를 쉽게 작성.
# future: 아직 오지 않았지만 '미래에' 도착할 결과 = 신청과 결과 수령 플로우가 불연속적 (비동기)


work_list = [1000000,10000000, 100000000] # 계산이 많은 CPU 작업 (함수로 [func1, func2] 넣을수도 있음)
                            # 스레드 1은 첫번째 1000, 스레드 2는 10000 각자 일 어사인됨
                            # 스레드가 각각 동시에 일하는 것을 기대
def sum_gen(n):
    return sum(n for n in range(1, n+1))

def main():
    threads = min(10, len(work_list)) # 스레드 갯수 미정일 때 정하는거 컴퓨터에 위임
    start_time = time.time()

    # 결과. 동시성 작업 만드는 스텝
    with ThreadPoolExecutor() as executor: # 멀티 프로세싱: ProcessPoolExecutor()
                                                # Executor는 지금 비어있는 워커 중 누구에게 배분할지, 대기시킬지 결정
                                                # ThreadPoolExecutor생성하면 내부에 워커 스레드 객체 생성하고, 스레드들은 아무 일도 안 하고 대기
        #   with : 블록 종료 시 자동으로 executor를 닫아서 스레드 정리해줌
        result = executor.map(sum_gen, work_list) # map: 작업 순서 정해줌. 즉시 실행

   
    end_time = time.time()
    msg = 'Result: {} Running Duration: {:.2f}s'
    print(msg.format(list(result), end_time - start_time))
    
    
# 메인함수에 진입점 알려줌. 시작 실행점    
if __name__== '__main__':
    main()  
    
    
# 이 코드가 작업을 기다렸다가 순차 실행하는데도 futures 비동기인 이유: 
# 메인 스레드에서 태스크 제출하면 -> T1/T2/T3 실행 여부, CPU를 누가 쓰는지, 언제 끝나는지 모두 메인스레드 통제 밖.
# map은 결과를 바로 주지 않는 대신, Future들의 iterator를 준다
# 그 결과 메인스레드는 자연히 다른 일 할 수 있어지니 non-blocking (= 제어권 되찾음)
# -> 제출 방식은 비동기/ 결과 다 나올때까지 list()로 기다리는건 동기
# -> 작업 순차 실행은 문제가 안됨. 비동기성 멀티 작업이라고 모든 스레드가 다 자기일 몰두해야 한다는건 착각. 모든 스레드가 다 cpu-bound라 하나 빼고 나머지 다 runnable 대기중인 것도 비동기성.
# -> 이 코드는 세 스레드 모두 CPU계산이 필요하니 멀티프로세싱이 더 나았겠다

# 멀티 스레드 내 모든 스레드가 시작됨. 다만 실행되는게 하나뿐이고 나머지는 대기중일뿐 (=runnable이지만 GIL없어서 대기중인 것)
# 참고: 대기중 (runnable) != I/O 중:
# 멀티 스레드에서 T1 : running, T2: runnable 이면 두 스레드는 GIL 경쟁중. 
# T1: running, T2: I/O 중 이면 GIL 경쟁 x.



# In[ ]:


# futures + wait (스레드 당 작업 시간 상한)

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
            print('Scheduled for {}:{}'.format(work, future)) # asyncio는 단일 스레드라서 그 순간 하나만 running, 나머지는 pending중
        result = wait(future_list, timeout = 5) # 작업 시간 각 5초 줌
        
        print('Successful tasks: '+ str(result.done)) # 성공 작업들
        print('Pending tasks: '+ str(result.not_done)) # 실패 작업들 (5초 이상 걸린건 실패로 간주)
        print([future.result() for future in result.done]) # 성공 태스크의 결과값 (합계)

    end_time = time.time()
    msg = 'Running Duration: {:.2f}s'
    print(msg.format(end_time - start_time))
    
    
if __name__== '__main__':
    
    # 메인 모듈 = Python 인터프리터가 1번 순서로 실행한 스크립트. 인터프리터가 '직접' 읽은 파일일 경우에만 실행하라.
    # 스크립트 내 import나 하위에서 읽어진 파일은 일단 스크립트 실행된 다음 불렸을거니까 그건 '처음' 실행 파일이 아님. 2번 순서 이상이겠지
    # 멀티 프로세싱의 경우 import나 하위에서 읽어진 파일은 문제가 있을 수 있어, 파이썬 인터프리터가 직접 읽은 파일일 경우만 실행하려는 코드
    # practice_intermediate.ipynb파일을 인터프리터가 읽으면 메인 파일이라고 간주할 것. 메인 파일의 속성 내 __name__은 __main__이라고 되있음  
    main()  
    
# 왜 __name__= 'main'이 없으면 에러나는지: 멀티프로세싱의 경우 자식 프로세스 생성하는데, 각 자식 프로세스는 메인 파일을 다시 읽어서 워커 스레드를 생성
# 만약 if __name__ == '__main__': 블록이 없으면, 부모에서 실행된 코드를 자식이 또 실행 -> 무한 루프 또는 BrokenProcessPool 발생 가능
    


# In[ ]:


# 만약 여러 다른 동작의 태스크를 처리하려면 리스트에 func를 넣을 수 있음

def func1():
    return sum(range(1, 2))

def func2():
    return sum(range(1, 3))

def func3():
    return sum(range(1, 4))

tasks = [func1, func2, func3]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(task) for task in tasks]  # map()도 비슷. 결과를 얻는 방식 차이

    results = [f.result() for f in futures]


# In[ ]:


# map 과 submit의 차이
# - map: 결과를 iterable 로 받음. 결과 받을때까지 기다리면서 이미 다 완료된 task부터 하나씩 흘려 받음.
# - submit: 결과를 Futures 로 받음 -> 비동기의 본질. 결과 아직 안 난 상태에서 Future만 (작업 확인서) 받고 완료되면 받으러 감. 아직 완성 안됐으므로 중간에 취소도 가능. 더 ㅁ



# - dead lock과 스레드의 연관성 
# - 데드락: 멀티 스레드에서 스레드끼리 코드가 꼬여서 서로가 가진 실행 결과만 기다림. (A를 실행하기 위해 B가 필요한데, B가 나오기 위해 A가 필요) 무한 정지.  
# 스레드간 실행 순서가 예측 불가 → 순환 대기 조건이 쉽게 생김. 스레드 갯수가 많을수록 발생 확률 높아짐.
# GIL 도 막아주지 못함 (A만 실행하게 하는데 A를 완료하려면 B 돌린 결과가 필요해)


# In[ ]:


# futures + as_completed (스레드 당 작업 시간 상한)

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed  


work_list = [100000,1000000, 10000000] # 어떤 작업부터 먼저 스케줄링 될지는 랜덤
                    # 먼저 끝나는 것부터 나옴
def sum_gen(n):
    return sum(n for n in range(1, n+1))

def main():
    # threads = min(10, len(work_list))
    start_time = time.time()    
    future_list = []
    
    
    # 작업 요청 제출 / 접수 확인증 발부
    with ProcessPoolExecutor() as executor:
        for work in work_list:
            future = executor.submit(sum_gen, work)
            future_list.append(future)
            print('Scheduled for {}: {}'.format(work, future))
   
            
        # 작업 리턴
        for future in as_completed(future_list): # 작업 후 future는 <Future at 0x1055eed40 state=finished returned int> 번호, 실행상태 리턴
            result = future.result() # 해당 future중 result만 뽑음
            done = future.done()
            cancelled= future.cancelled
            
        # as_completed vs. wait
        # wait: 5초라는 조건이 충족된 future들만 모아서 한번에 던짐
        # as_completed: 먼저 끝난 future부터 yield
        # 리스트 순서대로 작업 제출해도 시작하는 순서는 랜덤. 끝나는 순서만 알 수 있음 -> 작업 순서보다 done 여부가 더 중요


        # future 결과 확인
            print('Future Result: {}, Done: {}'.format(result, done))
            print('Future Cancelled: {}'.format(cancelled))
    
    end_time = time.time()
    msg = 'Runtime Duration: {:.2f}s'
    print(msg.format(end_time - start_time))

    
    
if __name__== '__main__':
    main()  


# In[ ]:


# asyncio: async/await 이용해 비동기성 코드 쉽게. 대부분 non-blocking I/O bound 용. 단일 스레드지만 대기 시간을 가장 효율적으로 쓸 수 있음

# 멀티 스레드를 만들지 않고, 코루틴만을 이용해 비동기성 달성. 단일 스레드 안에서 여러 코루틴을 스케줄링
# 힌 코루틴 I/O 기다리는 동안 다른 코루틴 실행 → 스레드 추가 없이도 동시에 여러 작업 수행한 것처럼 보임
# 이벤트 루프: asyncio 내 어떤 코루틴이 실행되고 기다릴지 관리하는 스케줄러. 어디에 맡길지, 그동안 뭘 실행할지, 언제 이 코루틴을 다시 깨울지 결정

# async의 장점: 
# 컨텍스트 스위칭 비용 없어 빠름. OS 개입 (멀티스레드는 time slice 이후 OS 인터프리터가 스레드를 바꾸는 거였음) 없이 바로 이동 가능하므로
# 기본적으로 I/O bound를 non blocking하는 것에 특화됐지만, CPU bound 작업은 계산 파트를 쪼개서 다른 코루틴에 주기적으로 양보하거나, 스레드/프로세스로 오프로드해서 단일 스레드로도 비동기성 구현 가능


# In[ ]:


async (코루틴)과 스레드는 역할이 다름. 코루틴은 제어 흐름 단위, 스레드는 실행 엔진, asyncio는 코루틴 관리 위해 만들어진 스케줄러.
OS가 운영하는 실행 엔진인 스레드 위에서 코루틴이 번갈아 올라탐. 스레드 위 코루틴을 asyncio가 activate시켜서 정지를 기점으로 쪼개 쓸 수 있음

스레드 내 코루틴의 코드 흐름은 직선 (코루틴 A가 await 만나 멈추면 코루틴 B 시작. A가 기다리는 결과는 나중에 이벤트 루프가 받으면 알려줌), 실행은 await마다 분기

async는 future같이 “결과를 나중에 받을 약속을 만드는 것”이 목적 (애초에 기다리는 시간을 활용하는 시스템도, 미래에 결과를 받을거라는 future가 이벤트 루프에 이미 등록된 상태이기때문에 안심하고 결과 받을 때까지의 시간을 활용하는거라서)

I/O bound 일 때: async+ 멀티스레드가 만나면 멀티스레드가 부족한 점을 async가 채워줘서 잘 맞음. 만약 멀티스레드만 있었으면 기다림이 언제인지 얼마나 걸리는지 추상적인 채라 다룰 수 없는데 async는 플래너이므로 작업 사이 기다림들을 명시적인 변수에 할당해서 코드화시켜 다룰 수 있게 함
->멀티스레드만 있었으면 작업 사이 기다림을 그냥 아무것도 못하고 날려버림. async는 기다리는 시간에 뭘 할지 넣을 수 있어서 효율적으로 코드 가능. 
멀티스레드는 여러 스레드 통해서 기다림 시간을 사용하려 하지만/ async는 한 스레드를 여러 코루틴이 쓰고 yield 작업 중단을 통해 (전 코루틴의 양보) 다음 코루틴으로 넘어가는 특성때문에, 작업 사이 기다림 시간을 애초에 구조화 할 수 있는 장점이 있었음. 

그 중 I/O 바운드 스레드가 대다수를 차지하는 멀티스레드여야만 함. CPU를 오랫동안 계산하는 스레드가 하나라도 있으면 GIL을 오랫동안 점유함. async는 스레드 사이를 메뚜기처럼 뛰어다니면서 정지 시간에 CPU 계산을 끼워넣는 구조인데, 오랫동안 GIL을 놔주지 않는 스레드가 있으면 사이사이 CPU 활용을 못함

CPU bound일 때 async+ 멀티스레드: 기다림이 없이 쉴 새 없이 계산하므로, 기다림을 쪼개 쓰는 async가 장점 발휘할 여지 없고 + 기다림 사이에 가벼운 CPU 작업을 해야하는데 다른 CPU 작업이 GIL을 안줘서 정지

async+ 멀티 프로세싱: 멀티 프로세싱에도 I/O bound는 존재하기 때문에 async는 그 기다림을 어떻게 쓸지 플래닝. CPU I/O 일 때 최적. blocking I/O 일때는 프로세싱이 너무 무거움.-> I/O 일때는 async+ 멀티스레드가 더 흔함

async만 쓰는 경우: CPU bound에 약하다. 동일 스레드 내 한 코루틴이 CPU를 0.1초만 잡고 있어도, 다른 코루틴들이 CPU가 필요할 때 와주지 못함. 0.1초는 기계 입장에서는 아주 길어서 그동안 다른 코루틴들 태스크 다 지연되고 결국 코루틴간 협력 관계 무너짐.
멀티 스레드라면 OS가 다른 스레드들 위해서 강제 전환하지만 async는 자발적 양보 시스템이므로 

-> async: 거의 기다리는 작업뿐일 때
async+ 멀티스레드: blocking I/O 함수 (urlopen) 섞여 있음 or CPU 계산은 아주 짧음. CPU계산은 스레드로 빼줌. 멀티스레드 단독으로 써도 이미 시간을 아껴주지만, asyncio를 쓰면 각 스레드의 코루틴 사이 정지 시간을 구조화하고 스레드마다 메뚜기짓을 해서 더욱 효율적으로 씀
async + 멀티프로세스: 많은 CPU 계산. CPU 계산은 프로세스로 격리




    
    🍳 상황 설정

요리사 = CPU

요리 단계 = 코드 실행

오븐/물 끓이기 = I/O (대기)

주방 관리자 = OS / 이벤트 루프

조리대 1개 = GIL

1️⃣ 멀티스레드 주방 (GIL 있는 파이썬)
구조

요리사 여러 명 (스레드 여러 개)

조리대는 1개뿐 (GIL)

실제 흐름

👨‍🍳 요리사 A
→ 고기 손질 (CPU 연산)
→ 조리대(GIL) 점유

👨‍🍳 A
→ 오븐에 넣음
→ 🔥 “20분 기다림”

🔓 이때 조리대를 비움 (GIL release)
→ 요리사 B가 조리대 사용 가능

👨‍🍳 B
→ 다른 요리 손질

오븐 완료
→ 관리자(OS)가 A 깨움
→ 다시 조리대 쟁탈전

왜 I/O-bound에 “괜찮냐면”

오븐 대기 중인 요리사는 조리대를 안 잡음

다른 요리사가 바로 일 가능

👉 GIL 때문에 막혔는데,
I/O 중엔 우연히 길이 열림

단점

요리사 수 늘수록:

동선 꼬임

충돌

관리 비용 ↑

조리대 쟁탈 발생

2️⃣ 코루틴 주방 (async / await)
구조

요리사 1명

조리대 1개

“알림 벨 달린 오븐” (이벤트 루프)

실제 흐름

👩‍🍳 요리 시작

고기 손질 (CPU)

오븐에 넣음

🔔

await oven.wait()


“이건 기다려야 하네.
끝나면 불러줘.”

바로 다음 요리 손질

🔔 오븐 완료 알림

다시 돌아와 플레이팅

핵심 포인트

요리사가 의도적으로 조리대를 양보

“기다림”이 명시적

관리자(OS)가 아니라
요리사가 흐름을 통제

3️⃣ 결정적 차이 (이게 본질)
멀티스레드

“기다리는 동안
다른 요리사라도 써야지”

코루틴

“이건 기다리는 게 본질이네
→ 기다림을 코드로 표현하자”


코루틴이 I/O-bound에 “더 적은 자원으로 동일한 정지 시간을 채워쓸 수 있음 (스레드보다 더 빠르기도 하고)


# In[ ]:


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

# await something: 



    return response.read()[0:5]
    


async def main(): # 돌아주는 스레드 생성해서 async로 넘김
    executor = ThreadPoolExecutor(max_workers=10)
    futures = [
        asyncio.create_task(fetch(url, executor)) for url in urls # url당 한 스레드 
             ]
    
    result = await asyncio.gather(* futures) # list 언패킹
    #gather가 하는 일:
# 여러 awaitable(Task/Coroutine)를 받는다
# 모두 완료될 때까지 대기한다 (모은다 = gather)
# 완료되면 결과를 리스트로 반환한다
    
    print(result)
    duration = timeit.default_timer - start
    print('Running Duration: ', duration)



if __name__ == '__main__':
    asyncio.run(main())


# In[ ]:


await something: something 다 할 때까지 이 포인트까지 (yield) 작업한 코루틴은 잠시 중단하겠다. 그리고 something 다 되면 다음 코루틴이 넘겨받는다.

1️⃣ await = “여기서 멈춰도 된다” 선언
상황

손님 주문:

스테이크

소스는 외부 업체에서 가져옴 (blocking)

코드 감각
sauce = await get_sauce()

주방 해석

총괄 셰프:
“소스 도착 전까지 이 요리는 멈춰도 됨”

소스 주문을 넣고

이 요리를 잠시 선반에 올려둠

다른 주문 처리로 이동

👉 await = 작업 중단 지점 설계

async def order_A():
    steak = await grill()
    plate(steak)

async def order_B():
    soup = await boil()
    serve(soup)


async def handle_order():
    sauce_task = asyncio.create_task(get_sauce())
    steak = grill_now()
    sauce = await sauce_task
    plate(steak, sauce)



await fetch_data()를 만나면

fetch_data() 실행 → Future / Task 객체 생성

“이 작업 끝나면 다시 불러줘”라고 이벤트 루프에 등록

task1 실행 중단

즉시 제어권을 이벤트 루프에 반환

이벤트 루프는 다른 task 실행

👉 결과가 왔는지는 상관없다


# In[ ]:


import asyncio
import timeit
from urllib.request import urlopen # urlopen은 blocking 함수. async만 쓴다면 이 코루틴 완료될 때까지 암것도 못함.
                                # 반면 asyncio는 I/O 중 다른 코루틴으로 변경 가능 (non-blocking) -> 안맞음
                                # 블로킹 함수는 스레드/프로세싱 풀에 떠넘기면서 blocking 함수를 더 빨리 처리 가능
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading


start = timeit.default_timer()
urls = ['http://naver.com', 'http://idpaper.com']


async def fetch(url, executor): 
    loop = asyncio.get_running_loop() # 지금 돌고 있는 이벤트 루프 가져옴
    response = await loop.run_in_executor(executor, urlopen, url)                                                     
                                            # run_in_executor : blocking library인 urlopen을 async 멀티 스레딩/멀티 프로세싱 환경에서도 blocking I/O는 해당 스레드/프로세스를 점유
                                            # 운 나쁘게 블록된 스레드가 이벤트 루프라면 스케줄링 멈춰서 코루틴 사이 대기 시간을 사용 불가능해짐 -> async 환경에서는 blocking I/O를 executor로 분리
                                            # blocking 함수를 멀티 스레딩/멀티 프로세싱에게 던져버리고 스케줄러 포함하는 스레드/프로세스는 포함 시키지 않아 스케줄러 정지 안되도록 함
                                            
                                            # loop.가 붙는 이유: “이 이벤트 루프"를 넘기겠다
    return response.read()[0:5]
    
    
async def main(): 
    executor = ThreadPoolExecutor(max_workers=10) # I/O bound 작업 이므로 멀티 스레딩 추천. CPU bound 아니면 멀티 프로세싱은 너무 무거움.
    futures = [
        asyncio.create_task(fetch(url, executor)) for url in urls # 일단 작업 요청 등록을 create_task로 함. 작업 요청 확인서인 future를 반환 받음.
             ]
    
    result = await asyncio.gather(* futures) # 한 리스트 내 여러 futures를 한 튜플로 언패킹
                                            # gather: 여러 코루틴/futures가 모두 완료될 때까지 대기하며, 완료된 것을 모음. 완료되면 결과를 리스트로 반환
    print(result)
    duration = timeit.default_timer - start
    print('Running Duration: ', duration)


if __name__ == '__main__':
    asyncio.run(main())

