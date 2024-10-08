'''
Q)  아래처럼 팀원끼리 조별 과제가 주어졌을때,
    팀원 이름과 수행할 업무를 랜덤으로 매칭시켜
    분담할 수 있게 코드를 구현해 봅시다.
    (Tip: 리스트, 집합 1개씩 선언)


    ↓ 실행화면(랜덤) ↓
    paul -> 발표
    smith -> 보고서 작성
    john -> 무임승차
    tyler -> 피피티
'''
names = ['paul', 'smith', 'john', 'tyler']
tasks = {'피피티', '발표', '보고서 작성', '무임승차'}

index = 0
for e in tasks:
    print(f'{names[index]} -> {e}')
    index+=1
print()

for a,b in zip (names,tasks):
    print(f'{a} -> {b}')
