#input은 입력되는 모든 것을 문자열로 취급
a=input()
print(a) #사용자 입력값이 출력된다

#프롬프트를 띄워서 사용자 입력 받기
number=input("숫자를 입력하세요:")
print(number)
#숫자를 입력하세요: #사용자 입력값이 출력된다

#큰따옴표로 둘러싸인 문자열은 +연산과 동일하다
print("life" "is" "too short")
print("life"+"is"+"too short")
#lifeistoo short
#lifeistoo short

#문자열 띄어쓰기는 콤마로 한다
print("life","is","too short")
#life is too short

#한 줄에 결괏값 출력하기
for i in range(10):
    print(i,end=' ')
#0 1 2 3 4 5 6 7 8 9
#띄어쓰기를 사용하기 위해 end를 사용해 끝 문자를 지정한다.