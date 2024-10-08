'''
# return문
    def f(x):
    ...
    return 리턴값
함수 내부에서 return문은 결과값을 함수 밖으로 전달하면서 함수를 종료한다.
'''
# 함수 선언
def get_add(x, y):
    return x+y

# 함수 호출
print(get_add(10, 20))
num = get_add(30, 40)
print(num)

# 두 실수의 합을 반환
num2 = get_add(3.5, 6.8)
print(num2, type(num2))

# 두 문자열을 이어 붙여서 반환
msg = get_add('여름', '가을')
print(msg, type(msg))
############################
def getAverage(a,b,c):
    sum = a+b+c
    return sum/3
print('평균은', getAverage(20, 20, 50))
############################
def good_day():
    print(' 리턴문 앞')
    return  '좋은 하루 보내세요!'
    print('리턴문 뒤')
print(good_day())
############################
# 함수의 다양한 리턴 타입
def f(x):
    return x, x*2, x*3
k = f(10)
print(k, type(k))

# 리스트 타입으로 리턴
def g(x):
    return [x, x*2, x*3]
print(g(20))
print('='*20)

#== 함수 내부에서 함수 호출 가능 ==#
# 함수 안에서 다른 함수를 호출할 수 있다.
def msg():
    print('아직 덥습니다')
def repeat(n):
    for i in range(n):
        msg()
repeat(4)

# 재귀 함수: 함수 안에서 본인을 호출할 수 있다.
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
print(fac(3))
'''
fac(3) = 3*fac(2) = 3*2*1*1
fac(2) = 2*fac(1) 
fac(1) = 1*fac(0)
fac(0) = 1
'''

