#for 변수 in [리스트,튜플,문자열] : 형태
'''
#i에 요소들이 차례로 대입되면서, print하면 출력된다.
test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

#one
#two
#three



#a리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 first와 last변수에 대입된다.
a= [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

#
#3
#7
#11



#"총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
marks = [90,25,67,45,80]
num = 0
for mark in marks :
    num+=1
    if mark >= 60 :
        print("%d학생은 합격입니다." %(num))
    else :
        print("%d학생은 불합격입니다." %(num))



#continue사용
marks = [90,25,67,45,80]
num = 0
for mark in marks :
    num+=1    
    if mark >= 60 :
        print("%d학생은 합격입니다." %(num))
    else :
        continue



#range함수
a=range(0,10) #0부터 10미만을 만들어준다.

add=0
for i in range(1,11):
    add=add+i
    print(add)
#1
#3
#6
#10
#15
#21
#28
#36
#45
#55



#range를 사용한 for문
marks = [90,25,67,45,80]
for num in range(len(marks)) : #len으로 0부터 5미만을 만듦
    if marks[num] >= 60 :
        print("%d학생은 합격입니다." %(num+1))




for i in range(2,10):
    for j in range(1,10) :
        print(i*j, end=" ") #매개변수 end를 넣어 준 이유는 해당 결괏값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서
    print('') #엔터
    
#2 4 6 8 10 12 14 16 18 
#3 6 9 12 15 18 21 24 27
#4 8 12 16 20 24 28 32 36
#5 10 15 20 25 30 35 40 45
#6 12 18 24 30 36 42 48 54
#7 14 21 28 35 42 49 56 63
#8 16 24 32 40 48 56 64 72
#9 18 27 36 45 54 63 72 81


#리스트 내포(list comprehension)


#a리스트 요소에 3을 곱해 result 리스트에 담음
a=[1,2,3,4]
result =[]
for num in a :
    result.append(num*3)

print(result)
#[3, 6, 9, 12]


#위의 소스를 리스트 내포를 사용하기
a=[1,2,3,4]
result=[num * 3 for num in a]
print(result)
#[3,6,9,12]


#짝수만 3을 곱하여 result 리스트에 담기
a=[1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
#[6,12]
#[표현식 for 항목 in 반복가능객체 if 조건문]
'''

#구구단을 리스트 내포를 사용하여 구현
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 
#15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
