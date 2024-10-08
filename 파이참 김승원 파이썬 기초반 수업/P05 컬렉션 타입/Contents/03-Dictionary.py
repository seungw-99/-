'''
# 딕셔너리(Dictionnary)
딕셔너리명 = {key:value, key:value...}
딕셔너리 특징: 순서X, key중복X, 변경O
'''
a = {'name': '너구리', 'birth': '5/1', 'age':10}
b = {0:'Today', 2:'is', 1:'Friday'}
c = {1:20, 2:40, 3:60}
d = {'num':100, 'num2':200}
e = {'pet':['dog', 'cat'], 'wild':('tiger', 'shark')}
print('딕셔너리a 개수:', len(a))
print('딕셔너리e 개수:', len(e))

# key로 value 접근
print(a['name'])
print(b[2])
print(c[1])
print(d['num2'])
print(e['pet'][0])
print('='*20)

#== 딕셔너리 데이터 추가, 수정, 삭제 ==#
## 추가
a['hobby'] = 'Youtube' # 딕셔너리명[새로운key] = value
print(a)
c[4] = 80
print(c)

## 수정
a['name'] = 'nuguri' # 딕셔너리명[기존key] = value
print(a)

## 삭제
del a['hobby'] # 해당 key와 value를 삭제
print(a)
del c[4]
print(c)
print()

#value만 가져오기
print(a.values())
print(c.values())
print(list(a.values()))
print(list(c.values()))
print(a.keys())
print()

# 딕셔너리 key 중복일 때
f = {'a':1, 'a':2}
print(f)

# 여러개 추가
f.update({'b':3, 'c':4})
print(f)