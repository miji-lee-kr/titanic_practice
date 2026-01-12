# 변수를 자동으로 대량 생성하려면

for i in range(1,3):
    for k in range(1,3):
        globals()['var_{}_{}'.format(i,k)] = i+k
        
print(globals())
print(var_1_1)