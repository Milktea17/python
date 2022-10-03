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

#문자열 슬라이싱으로 바꾸기
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

#위에서 0자리에 format넣는거랑 같은형식 (0(변수):<10)
print("{0:<10}".format("hi")) #'hi          '
print("{0:>10}".format("hi")) #'          hi'
print("{0:^10}".format("hi")) #'     hi     ' 가운데정렬
print("{0:=^10}".format("hi")) #====hi====
print("{0:!<10}".format("hi")) #hi!!!!!!!!

y = 3.42134234
print("{0:0.4f}".format(y)) #3.4213

print("{{ and }}".format())
print("="*40)

#f 문자열 포매팅

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')
print(f'나는 내년이면 {age+1}살이 된다.')

d={'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":!<10}')
print("="*40)

#문자 개수 세기(문자열에서 해당 문자 개수 세기)
a="hobby"
print(a.count('b')) #2

#위치 알려주기1(find)
a="Python is the best choice"
print(a.find("b")) #14 처음으로 나온 위치 반환(0~)
print(a.find("k")) #-1 (없을경우에는 -1리턴)

#위치 알려주기2(index)
print(a.index("b")) #14 처음으로 나온 위치 반환(0~)
#print(a.index("k")) #find와 달리 없을 경우에는 error발생
print("="*40)

#문자열 삽입(join)
print(",".join('abcd')) #a,b,c,d 각 문자 사이에 ,가 삽입됨. 

#소문자를 대문자로(upper)
a='hi'
print(a.upper())

#대문자를 소문자로(lower)
a="HI"
print(a.lower())
print("="*40)

#왼쪽 공백 지우기(lstrip)
a=" hi "
print(a.lstrip()) #'hi '

#오른쪽 공백 지우기(rstrip)
print(a.rstrip()) #' hi'

#양쪽 공백 지우기(strip)
print(a.strip()) #'hi'
print("="*40)

#문자열 바꾸기(replace)
a="Life is too short"
print(a.replace("Life", "Your leg")) #Your leg is too short

#문자열 나누기(split)
print(a.split()) #['Life', 'is', 'too', 'short'] 괄호를 비울 시, 공백(스페이스, 탭, 엔터 등)을 기준

b="a:b:c:d"
print(b.split(":")) #['a', 'b', 'c', 'd']