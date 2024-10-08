#== 컬렉션 타입 관리 함수 ==#
# enumerate 함수
# 1개의 컬렉션 타입에서 인덱스와 데이터를 쌍으로 묶어서 사용
alp = ['A', 'B', 'C']
print(list(enumerate(alp)))

for tup in enumerate(alp):
    print(tup)
num1, num2 = 10, 20
print(num1, num2)

for a, b in enumerate(alp):
    print(a, b)

score_list = [100,95,90,80]
for rank, score in enumerate(score_list): # (0, 100)..
    print(f'{rank}등: {score}점')
print('='*20)

# zip 함수
# 여러개의 컬렉션 타입을 합쳐서 하나로 사용
day = ['금', '토', '일']
food = ('피자', '햄버거', '치킨')
des = {'커피', '밀크티', '젤라또'}
for a,b,c in zip(day, food, des): # ('금', '피자', '?')
    print(f'{a}요일 메뉴: {b}, 후식: {c}')