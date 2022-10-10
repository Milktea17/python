#if문
money = True
if money:
    print("택시를")
#print("타고") #IndentationError if: 아래는 들여쓰기 해야함
#        print("가라") #IndentationError if: 같은 너비로 들여써야한다.
print("="*40)

#아래와 같이 같은 너비로 들여쓰기를 하면 오류가 나지 않는다.
if money:
        print("택시를")
        print("타고") 
        print("가라")
print("="*40)