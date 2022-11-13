#def는 함수를 만날 때 사용하는 예약어
#일반적인 함수
def add(a,b):
    return a+b

a=3
b=4
c=add(a,b)
print(c)
#7
print("="*40)
#=============================================

#입력값이 없는 함수
def say():
    return 'Hi'

print(say())
#Hi
print("="*40)
#=============================================

#결괏값이 없는 함수
def add(a,b):
    print("%d,%d의 합은 %d입니다"%(a,b,a+b))

print(add(3,4))
#3,4의 합은 7입니다
#None //리턴값이 없어서 None을 return한다
print("="*40)
#=============================================

#입력값도 결괏값도 없는 함수
def say():
    print('Hi')
    
say()
#Hi
print("="*40)
#=============================================

#매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result=add(a=3,b=7)
print(result)
#10
print("="*40)
#=============================================

#여러 개의 입력값을 받는 함수 만들기
def add_many(*args): # *을 붙여 튜플로 만든다
    result = 0
    for i in args:
        result = result+i
    return result

result = add_many(1,2,3)
print(result)
#6

def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result+i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result*i
            
    return result

result=add_mul('add',1,2,3,4,5)
print(result)
result=add_mul('mul',1,2,3,4,5)
print(result)
#15
#120
print("="*40)
#=============================================
