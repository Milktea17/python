#리스트로 집합 만들기
s1 = set([1,2,3]) 
print(s1) #{1, 2, 3}

#문자열로 집합 만들기
s1 = set("Hello")
print(s1) #{'H', 'l', 'e', 'o'} #집합은 중복을 비허용, 순서가 없다. - 딕셔너리와 비슷한 특징
print("="*40)

#집합을 인덱싱으로 접근하기
s1 = set([1,2,3])
l1 = list(s1)
print(l1) #[1,2,3] 
print(l1[0]) #1 인덱싱으로 접근하려면 리스트나 튜플로 변환해야한다.
t1 = tuple(s1)
print(s1) #{1, 2, 3}
print(t1[0]) #1
print("="*40)

#집합 사용하기 - 교집합,합집합,차집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합
print(s1&s2) #{4,5,6}
print(s1.intersection(s2)) #{4,5,6}
print("="*40)

#합집합
print(s1|s2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print("="*40)

#차집합
print(s1-s2) #{1, 2, 3}
print(s2-s1) #{8, 9, 7}
print(s1.difference(s2)) #{1, 2, 3}
print(s2.difference(s1)) #{8, 9, 7}
print("="*40)

#값 1개 추가하기
s1=set([1,2,3])
s1.add(4)
print(s1) #{1, 2, 3, 4}

#값 여러개 추가하기
s1=set([1,2,3])
s1.update([4,5,6])
print(s1) #{1, 2, 3, 4, 5, 6}

#특정 값 제거하기
s1=set([1,2,3])
s1.remove(2) # 제거할 값
print(s1) #{1,3}


