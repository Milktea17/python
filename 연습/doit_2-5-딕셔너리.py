#딕셔너리
dic = {'name':'pey', 'phone':'0119993323', 'birth':'0118'}

#value에 리스트도 넣을 수 있다.
a={'a':[1,2,3]}

#딕셔너리 쌍 추가
a={1:'a'}
a[2]='b'
print(a) #{1:'a', 2:'b'}

a['name'] = 'pey'
print(a) #{1: 'a', 2: 'b', 'name': 'pey'}

#딕셔너리 요소 삭제하기
del a[1]
print(a) #{2: 'b', 'name': 'pey'}

#딕셔너리에서 key의 value를 얻기
print(a['name']) #pey

a={2:'a', 1:'b'}
print(a[2]) #a 변수의 index가 아닌 key값인것 주의
print("="*40)


#주의사항1
a={1:'a', 1:'b'}
print(a[1]) #b 동일한 key가 여러개면 1개를 제외하고 무시

#주의사항2
#a={[1,2]:'hi'} #key값은 리스트로 사용할 수 없다.
b={(1,2):'hi'} #key값으로 튜플은 사용할 수 있다
#리스트와 튜플의 차이인 고정특징 유무 차이때문이다.
print("="*40)


#key 리스트 만들기
a={'name':'pey', 'phone':'0119993323', 'birth':'0118'}
print(a.keys()) #dict_keys(['name', 'phone', 'birth']) key가 모아진 리스트(dict_keys)를 출력한다.
print(list(a.keys())) #['name', 'phone', 'birth']

#value 리스트 만들기
print(a.values()) #dict_values(['pey', '0119993323', '0118'])
print(list(a.values())) #['pey', '0119993323', '0118']

#key,value 쌍(items) 리스트 만들기
print(a.items()) #dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '0118')])
print(list(a.items())) #[('name', 'pey'), ('phone', '0119993323'), ('birth', '0118')]

#key:value 쌍 모두 지우기
a.clear()
print(a) #{}
print("="*40)

#key로 value얻기
a={'name':'pey', 'phone':'0119993323', 'birth':'0118'}
print(a.get('name')) #pey
print(a.get('key')) #None a['key']를 사용했다면 실행시 key오류가 나는데 함수 사용시에는 None반환
#print(a['key']) #Key Error

#만약 None이 아닌 값을 출력하게 하려면 두번째 파라미터에 원하는 값 입력
print(a.get('key','default')) #default

#해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in a) #True