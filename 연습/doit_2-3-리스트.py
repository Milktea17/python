#리스트의 인덱싱
a = [1,2,3]
print(a) #[1,2,3]
print(a[0]) #1
print(a[0]+a[2]) #4
print(a[-1]) #3 -1 : 마지막 요소값

a=[1,2,3,['a','b','c']]
print(a[-1]) #['a','b','c']
print(a[-1][0]) #a

a=[1,2,['a','b',['Life','is']]]
print(a[-1][-1][0]) #Life

#리스트의 슬라이싱
a=[1,2,3,4,5]
print(a[0:2]) #[1,2]

a="12345"
print(a[0:2]) #12

b=a[:2]
c=a[2:]
print(b) #12
print(c) #345

a=[1,2,3,['a','b','c'],4,5]
print(a[3][:2]) #['a','b']

#리스트 더하기
a=[1,2,3]
b=[4,5,6]
print(a+b) #[1, 2, 3, 4, 5, 6]

#리스트 반복하기
a=[1,2,3]
print(a*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 길이 구하기
print(len(a)) #3

#문자와 숫자를 결합하려면
print(str(a[2])+"hi") #3hi

#리스트에서 값 수정하기
a[2]=4
print(a) #[1, 2, 4] 

#리스트에서 값 삭제하기(del)
del a[1]
print(a) #[1,4]

a=[1,2,3,4,5]
del a[2:]
print(a) #[1,2]

#리스트에 요소 추가(append)
a=[1,2,3]
a.append(4)
print(a) #[1,2,3,4]

a.append(['a','b'])
print(a) #[1,2,3,4,['a','b']]

#리스트 정렬(sort)
a=[1,4,3,2]
a.sort()
print(a) #[1,2,3,4]

a=['a','c','b']
a.sort()
print(a) #['a','b','c']

#리스트 뒤집기(reverse)
a.reverse()
print(a) #['c','b','a']

#위치 반환(index)
a=[1,2,3]
print(a.index(3)) #2 3의 index를 반환

#리스트에 요소 삽입(insert)
a.insert(0,4) #0번째에 4삽입
print(a) #[4,1,2,3]

a.insert(3,5)
print(a) #[4,1,2,5,3]

#리스트 요소 제거(remove)
a=[1,2,3,1,2,3]
a.remove(3)
print(a) #[1,2,1,2,3] 첫번째 나오는 3을 삭제

#리스트 요소 끄집어내기(pop)
a=[1,2,3]
print(a.pop(2)) #3
print(a) #[1,2]

#리스트에 포함된 요소의 개수 세기
a=[1,2,3,1]
print(a.count(1)) #2

#리스트 확장(extend)
a=[1,2,3]
a.extend([4,5]) #리스트를 붙일 때 사용
print(a) #[1,2,3,4,5]
a+=[6,7]
print(a) #[1,2,3,4,5,6,7]