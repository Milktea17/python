#2-2

# ""안의 '
food = "Python's favorite food is perl"
print(food)
print("="*40)

# ''안의 "
say = '"Python is very easy." he says.'
print(say)
print("="*40)

# \로 포함시키기
food1 = 'Python \'s favorite food is perl'
print(food1)
print("="*40)

#이스케이프 코드(\n) 로 줄바꾸기
multiline = "Life is too short\nYou need Python"
print(multiline)
print("="*40)

#''' 또는 """로 줄바꾸기
multiline2 = '''
Life is too short
You need python
'''
print(multiline2)
print("="*40)

#문자열 연결하기
head = "Python"
tail = " is fun"
print(head+tail)
print("="*40)

#문자열 곱하기
a = "python"
print(a*2) #이거 신기하다
print("="*40)

#문자열 길이 
alen = len(a)
print(alen)
print("="*40)

#문자열 인덱싱
print(head[-1]+head[-2]) #뒤부터 읽음
print("="*40)

#문자열 슬라이싱
print(head[0:3]) #[주의] 0<= 값 <3 Pyt
print(head[0:]) #Python
print(head[:6]) #Python
print(head[:]) #Python
print(head[:-1]) #Pytho
print("="*40)

#문자열 슬레이싱으로 바꾸기
pithon = "pithon"
print(pithon[0]+'y'+pithon[2:])
print("="*40)

#문자열 포매팅
print("I eat %d apples." %3)
print("I eat %s apples" %"five")
number=3
print("I eat %d apples" %number)
day="three"
print("I ate %d apples. so I was sick for %s days."%(number,day))
print("="*40)

#포맷코드와 숫자 사용
print("%10s" % "hi") #        hi
print("%-10sjane" % "hi") #hi        jane // hi를 (-)왼쪽으로 10정렬 시켜서
print("="*40)

#포맷 함수 사용
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples".format(number))
print("I eat {0} apples. so I was sick for {1} days.".format(number,day))
print("I eat {number} apples. so I was sick for {day} days.".format(number=10,day=3))
print("I eat {0} apples. so I was sick for {day} days.".format(10,day=3))
print("="*40)

