#import는 이미 만들어놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
import mod1
print(mod1.add(3,4)) #7
print(mod1.sub(4,2)) #2

#모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 사용하고 싶을 때
from mod1 import add 
print(add(3,4)) #7

#모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 사용하고 싶을 때
#1개가 아닌 다수의 함수 사용시
from mod1 import add,sub
from mod1 import *

'''
print(add(1, 4))
print(sub(4, 2))
를 mod1.py에 넣을 시 import할 때 오류
if __name__ == "__main__" 를 써야한다.
'''

print("="*40)
#=============================================

import mod2
a=mod2.Math()
print(a.solv(2)) #12.566368

print(mod2.add(mod2.PI,4.4)) #7.5415920000000005
