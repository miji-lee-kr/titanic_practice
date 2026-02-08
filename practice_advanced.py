def smile():
    print('smile')

def angry():
    print('angry')
    
def love():
    print('love')
    
    
# smile()
# angry()
# love()

# 재사용을 피하기 위해 함수 재정의

def copyright_func(func):
    def new_func():
        print('copyright')
        func()
    return new_func


love = copyright_func(love)
love()


# class Emoji:
#     def __init__(self, name):
#         self._name = name
        
#     def copyright(self):
#         print(f'{self._name} with copyright')
        

# class Open(Emoji):
#     cnt = 0
#     def __init__(self, name, model):
#         super().__init__(name)
#         self._model = model
#         Open.cnt += 1
        
#     def copyright(self):
#         print(f'{self._name} from {self._model}')
        
#     @classmethod
#     def total_cnt(cls):
#         print(f'{cls.cnt} is total model')


# smile_e = Emoji('smile')
# angry_e = Emoji('angry')
# smile_o = Open('smile', 'samsung')
# angry_o = Open('angry', 'iphone')

# smile_o.copyright()
# Open.total_cnt()