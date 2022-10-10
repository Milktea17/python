#리스트를 복사하고자 할 때
a=[1,2,3]

b=a #이렇게 사용하면 가리키는 대상이 동일하다
print(id(a)) #2493059822208
print(id(b)) #2493059822208

a[1]=4 # a와 b 동일한 리스트를 가리키기 때문에 둘다 값이 변한다.
print(a) #[1, 4, 3]
print(b) #[1, 4, 3]
print("="*40)

#[:]이용
a=[1,2,3]
b=a[:] #복사 / 다른값을 가리킴
a[1]=4
print(a) #[1, 4, 3]
print(b) #[1, 2, 3]

#copy 모듈 이용
from copy import copy #copy를 쓰기 위해
a=[1,2,3]
b=copy(a) #복사 / 다른값을 가리킴
print("="*40)

#튜플로 값 대입하기
a,b=('python','life')
print(a+' '+b)

#괄호를 생략한 튜플로 값 대입하기
(a,b)='python', 'life'
print(a+' '+b)

#리스트로 값 대입하기
[a,b]=['python','life']
print(a+' '+b)