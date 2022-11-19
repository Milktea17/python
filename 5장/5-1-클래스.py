#사칙연산 클래스 만들기

class FourCal():
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
        
a=FourCal()
a.setdata(4,2)
print(a.first) #4
print(a.second) #2

print(a.add()) #6

b = FourCal()
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
