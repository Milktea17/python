#Q1.주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(num):
    if (num%2)==1 :
        #print("%d is odd"%num)
        return True
    else:
        #print("%d is even"%num)
        return False
        
print(is_odd(2))
#False
print("="*40)
#=============================================

#Q2.입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
#(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# 평균 값을 구할 때 len 함수를 사용해 보자.
def num_avg(*args):
    num=0
    for i in args:
        num+=i
    return num/len(args)

print(num_avg(1,2,3))
#2.0
print("="*40)
#=============================================

#Q3. 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램의 오류 수정
'''
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2) #int 캐스팅
print("두 수의 합은 %d 입니다" % total) #출력시 %d사용
print("="*40)
'''
#=============================================

#Q4. 출력결과가 다른 한 개
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
#A4. 3번째는 ,로 인해 띄어쓰기가 들어간다.
print("="*40)
#=============================================

#Q5. 파일을 읽어서 출력하는 프로그램의 오류 수정

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() 

f2 = open("test.txt", 'r')
print(f2.read())

#A5. 파일을 닫아줘야 저장이 된다.
print("="*40)
#=============================================

#Q6. 사용자의 입력을 파일에 저장하는 프로그램 작성
f1=open('input.txt','a')
f1.write(input())
f1.close()

print("="*40)
#=============================================
