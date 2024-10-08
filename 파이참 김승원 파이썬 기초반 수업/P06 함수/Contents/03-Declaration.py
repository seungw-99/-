'''
함수 선언하기(function declartion)
# 함수 입출력 흐름
(입력) -> 함수 -> (출력)
(매개변수)        (리턴값)

#함수 구성 경우의 수
리턴값 매개 변수   함수 선언
x      x      f(): ...
o      x      f(): ..return a
x      o      f(num): ...
o      o      f(num): ..return a

# 함수 만들기
1. 만드려 하는 함수의 기능을 결정한다.
2. 기능에 맞는 함수 이름을 정한다.
3. 리턴값(출력)과 매개 변수(입력)를 고려하여 함수를 만든다.
4. 함수 이름과 매개 값을 일치 시켜 함수를 호출한다.
'''
# 리턴X, 매개 변수X 함수
# 예제1) '안녕하세요' 문자열을 5번 출력하는 함수를 만드시오.
def hello():
    # for i in range(5):
    #     print('안녕하세요')
    print('안녕하세요\n'*5)
hello()

# 리턴O, 매개 변수X
# 예제2) '감사합니다' 문자열을 반환하는 함수를 만들고 출력문으로 확인하시오.
# 만들고 출력문으로 확인하시오.
def get_thank():
    return '감사합니다'
print(get_thank())

# 리턴x, 매개 변수o
# 예제3) 매개변수로 문자열과 숫자를 입력받고,
# 받은 숫자의 횟수만큼 받은 문자열 내용을 출력하는 함수를 작성하시오.
def repeat_msg_byNum(msg, num):
    for i in range(num):
        print(msg)
repeat_msg_byNum('9월', 2)
repeat_msg_byNum(num=3, msg='가을겨울') # (매개 변수 = 매개 값) 전달

# 리턴o, 매개 변수o
# 예제4) 매개변수로 네 수를 입력받고 평균값을 리턴하는 함수를 작성하시오.
def getAvg(a,b,c,d):
    return (a+b+c+d)/4
print(getAvg(10, 20, 30, 40))

# 매개 변수로 리스트를 입력받고 리스트의 평균값을 리턴하는 함수
def average(a):
    return sum(a)/len(a)
k = [1, 4, 2, 5, 2, 6, 20, 40]
print(average(k))

