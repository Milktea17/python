#사칙연산 클래스 만들기

class FourCal():
    def __init__(self,first,second):
        self.first=first
        self.second=second
    
    def setdata(self,first,second):
        self.first=first #self객체에 생성되는 객체변수 first
        self.second=second
        #self:호출한 객체 자신이 전달된다
    
    def add(self):
        return self.first+self.second
    
    def mul(self):
        return self.first*self.second
    
    def sub(self):
        return self.first-self.second
    
    def div(self):
        return self.first/self.second
        
a=FourCal(4,2)
a.setdata(4,2)
print(a.first) #4
print(a.second) #2

print(a.add()) #6

b = FourCal(3,8)
b.setdata(3, 8)

print("="*40)
#=============================================

print(a.add()) #6
print(a.mul()) #8
print(a.sub()) #2
print(a.div()) #2.0
print(b.add()) #11
print(b.mul()) #24
print(b.sub()) #-5
print(b.div()) #0.375

print("="*40)
#=============================================

#생성자
#setdata 메서드를 수행하지 않고 add메서드를 수행하면 객체변수가 없어서 오류 발생
#생성자란 객체가 생성될 때 자동으로 호출되는 메서드.

#__init__을 사용하면 객체가 생성되는 시점에 first,second값을 넣어줘야 한다.

#a=FourCal()가 아닌 a=FourCal(4,2)로만 쓸 수 있다.

#=============================================

#클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        return self.first*self.second
    
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first/self.second
    
#class 클래스이름(상속할 클래스 이름)

#상속한 클래스의 기능을 모두 사용할 수 있다.
c=MoreFourCal(3,4)
print(c.add()) #7
print(c.mul()) #12
print(c.sub()) #-1
print(c.div()) #0.75

print(c.pow()) #12

print("="*40)
#=============================================

#메서드 오버라이딩(Overriding 덮어쓰기)
#부모클래스의 메서드 대신 오버라이딩 당한 메서드가 호출된다.
#=============================================

#클래스 변수
class Family:
    lastname="김" #클래스 안에 변수를 선언하여 생성함
    
print(Family.lastname) #김

Family.lastname = "박"
print(Family.lastname) #박
#클래스 객체로 만든 lastname값도 모두 변경된다.