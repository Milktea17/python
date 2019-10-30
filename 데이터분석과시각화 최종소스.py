import csv
import matplotlib.pyplot as plt

f = open('data.csv', 'rt', encoding='UTF8')

data = csv.reader(f)
next(data)
data = list(data)

pivot = []

name = '도담동'

for row in data :
    if name in row[0] : #도담동이면
        for i in range(3,len(row)) : #3번째부터 row의 문자열길이-1까지
            pivot.append(int(row[i])/int(row[2])) #pivot리스트에 담음
mn = 1
result_name='리스트'
for row in data : #data를 돌면서 가장 비슷한 지역 찾기
    s = 0
    for i in range(3, len(row)) : 
        row[i] = int(row[i])/int(row[2])
        tmp = (row[i] - pivot[i-3]) ** 2 #data 돌면서 찾는 지역(pivot)과 입력받은 지역(tmp)의 오차구함
        s = s + tmp
    if s < mn and (name not in row[0]) : #도담동이 아닌 최솟값일때의 지역을 구하기 위해
        result = []
        for i in range(3, len(row)) :
            result.append(row[i])
        mn = s            
        result_name = row[0]
            
#plt.rc('font', family = 'NanumGothic') #rc(): 글꼴바꾸기
#plt.style.use('ggplot') #stype.use() 그래프 스타일 조정
plt.figure(dpi=300) #figure() : 해상도조정
plt.plot(pivot, label = name) #도담동 
plt.plot(result, label = result_name) #도담동이랑 비슷한 지역
plt.legend() #legend() : 범례표시, 괄호가 비면 기본값이다
plt.savefig('stage6.png') #그래프를 이미지 파일로 나타내는 코드
plt.show()
