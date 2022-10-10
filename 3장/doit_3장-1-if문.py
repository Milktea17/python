#if문
money = True
if money:
    print("택시를") 
#print("타고") #IndentationError if: 아래는 들여쓰기 해야함
#        print("가라") #IndentationError if: 같은 너비로 들여써야한다.
print("="*40)
#택시를

#아래와 같이 같은 너비로 들여쓰기를 하면 오류가 나지 않는다.
if money:
        print("택시를")
        print("타고") 
        print("가라")
print("="*40)
#택시를
#타고
#가라

#and, or, not
money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고 가라")
else :
    print("걸어가라")
#택시를 타고 가라
print("="*40)

# x in s, x not in s
#리스트
print(1 in [1,2,3]) #True
print(1 not in [1,2,3]) #False

#튜플
print('a' in ('a','b','c')) #True

#문자열
print('j' not in 'python') #True
print("="*40)

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass #아무런 일도 하지 않도록 할 때
else :
    print("카드를 꺼내라")
print("="*40)

#elif
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else :
    print("걸어가라")
print("="*40)
#걸어가라

#if문을 한 줄로 작성하기
pocket = ['paper','money','cellphone']
if 'money' in pocket : pass
else : print("카드를 꺼내라")
print("="*40)