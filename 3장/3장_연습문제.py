#Q1.다음 코드의 결괏값은 무엇일까?

from re import S


a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#A1.shirt
#첫번째줄 - wife가 a에 있으면 wife출력
#두번째줄 - python이 a에 있고 you가 a에 없을때 python 출력
#세번째줄 - a에 shirt가 없으면 shirt출력
#네번쨰줄 - a에 need가 있으면 need출력
#다섯번째줄 - 4가지 조건을 하나도 충족하지 못할 시 none출력

#세번째 if 조건에 만족하여 shirt출력한다
print("="*40)


#Q2.while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
num = 1
result=0
while num<=1000:
    if num %3 == 0:
        result+=num
    num+=1

print(result)
#A2.166833
print("="*40)

#Q3.while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
num = 1
while num <=5:
    print("*"*num)
    num+=1

#A3.
#*
#**
#***
#****
#*****
print("="*40)


#Q4.for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1,101):
    print(i)
#A4. 1부터 100까지 각 라인마다 출력
print("="*40)


#Q5.A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#for문을 사용하여 A 학급의 평균 점수를 구해 보자.

score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for s in score :
    sum+=s

print("평균점수 : %d"%(sum/10))
#print("평균점수 : %d"%(sum/len(score))) //풀이대로

#A5. 평균점수 : 79
print("="*40)

#Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
#위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
        
result = [n*2 for n in numbers if n%2 == 1]
print(result)

#A6.[2, 6, 10]