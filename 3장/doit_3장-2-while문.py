''''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다" %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#나무를 1번 찍었습니다
#나무를 2번 찍었습니다
#나무를 3번 찍었습니다
#나무를 4번 찍었습니다
#나무를 5번 찍었습니다
#나무를 6번 찍었습니다
#나무를 7번 찍었습니다
#나무를 8번 찍었습니다
#나무를 9번 찍었습니다
#나무를 10번 찍었습니다
#나무 넘어갑니다.
print("="*40)
#===========================================================

#사용자가 값 4를 입력하지 않으면 계속해서 prompt를 출력
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number :"""

number = 0
while number !=4:
    print(prompt)
    number = int(input())

print("="*40)
#===========================================================

#자판기, break
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee-1
    elif money < 300:
        print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
        coffee = coffee-1
    else :
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
        
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

print("="*40)
#===========================================================
'''
#continue
a = 0
while a<10:
    a+=1
    if a%2 == 0: continue
    print(a)

#1
#3
#5
#7
#9