#try, except문

#try :
#except [발생오류 [as 오류변수]] :

#try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.

#=============================================

#1. try, except만 쓰는 방법
#try:
#except:
#오류 종류에 상관없이 오류가 발생하면 except 블록 수행

#2. 발생 오류만 포함한 except문
#try:
#except 발생오류:
#오류가 발생했을 때 except문에 미리 정해 놓은 오류와 동일한 경우에 except 블록 수행

#3. 발생 오류와 오류 변수까지 포함한 except문
#try:
#except 발생오류 as 오류변수:
#두번째 경우에서 오류의 내용까지 알고싶을 때 사용

try:4/0
except ZeroDivisionError as e:
    print(e)
#division by zero

#오류변수 e에 담기는 오류 메시지를 출력할 수 있다.
print("="*40)
#=============================================

#try .. finally
#예외 발생 여부에 상관없이 항상 수행된다.

try:
    f=open("foo.txt",'w')
finally:
    f.close()

#=============================================

#여러개의 오류 처리하기

#try:   
#except 발생오류1:
#except 발생오류2:

try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
#인덱싱 할 수 없습니다.
#인덱싱 에러가 먼저 발생하므로 인덱싱 오류만 출력된다.

#2개이상의 오류를 동일하게 처리하기 위해서는 괄호를 사용해 묶는다.
try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#list index out of range
print("="*40)
#=============================================

#try ... else

#try:
#except [발생오류[as 오류변수]]:
#else:

#try문 수행중 오류가 발생하면 except절이 수행되고 오류가 없으면 else절이 수행된다.

try:
    age=int(input("나이를 입력하세요: "))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age<=18:
        print('미성년자는 출입 금지입니다.')
    else:
        print('환영합니다')

#input 입력시 숫자가 아닌 다른 값을 입력하면 아래와 같이 출력됨.
#입력이 정확하지 않습니다.

#=============================================

#오류 회피하기 : pass
try:
    f=open('없는파일','r')
except FileNotFoundError:
    pass

#=============================================

#오류 일부러 발생시키기 : raise

class Bird:
    def fly(self):
        raise NotImplementedError
#bird에서 fly를 구현하지 않으면 error가 발생하게 함

class Eagle(Bird):
    pass

eagle=Eagle() #Bird 클래스의 fly메서드가 수행되면서 NotImplementedError에러가 발생한다.
eagle.fly()


class Eagle(Bird):
    def fly(self): #Eagle에서 Bird를 상속받으면서 오버라이딩해서 오류가 나지 않는다.
        print("very fast")

eagle=Eagle()
eagle.fly()

#very fast
print("="*40)
#=============================================

#예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)
    
say_nick("천사")
say_nick("바보")

#천사
#에러발생-raise MyError()에서.

try:
    say_nick("천사")
    say_nick("바보")
except:
    print("허용되지 않는 별명입니다.")
    
#천사
#허용되지 않는 별명입니다.

#오류 메시지를 사용하고 싶다면
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e) #에러 메시지가 출력되지 않는다.

#    def __str__(self):
#        return "허용되지 않는 별명입니다"
#만약 에러 메시지를 출력하고 싶으면 위의 __str__을 MyError에 선언해줘야한다.
