'''
# 함수(function)
함수는 어떤 기능을 수행하는 실행문들의 모음이다.
한번 작성된 함수는 여러 번 재사용 가능하다.
함수 작성시 입력 매개 변수나 리턴값 반환 여부를 선택 가능하다.

1. 함수 선언
    def 함수명(매개변수..):
        실행문..

함수를 선언 하여 '함수 명'이 어떤 기능들을 수행 하도록 정한다(define).

2. 함수 호출
    함수명(매개값..)

# 매개 변수(parameter)
함수를 실행할 때 필요한 데이터(매개값)를 외부로 부터 입력 받기 위한 변수
없거나 여러개 작성 가능
인자(argument) = 인수 = 매개값

# 기본 매개 변수
매개 변수에 초기값을 미리 설정해놓는 경우
'''
# 함수 선언
def hello(): # 매개변수 없음
    print('안녕하세요')

# 함수 호출
hello() # 매개값 필요x
hello()
#########################
# 함수 선언
def today(a): # 매개 변수 1개
    print('Today is', a)

# 함수 호출
# today() # 에러: 매개값 필요
today('monday') # 매개값 1개 필요
today('fall')

#########################
# 함수 선언
def add(x,y): # 매개 변수 2개
    print('두 수의 합:', x+y)

# 함수 실행
add(5, 10)
num1 = 100
num2 = 200
add(num1, num2)
add(50, num2)
# add(10)
# add(10, '가을') # 에러: 매개값 타입 불일치
############################
def is_discount(price):
    if price>=30000:
        print('배송비 무료입니다')
    else:
        print('배송비 2500원 입니다')
is_discount(50000)
is_discount(30000)
is_discount(10000)
############################
def repeat(times):
    for i in range(times):
        print('9월 17일 추석')
repeat(3)
############################
# 기본 매개 변수 사용
def discount(price, rate=0.1):
    print('할인적용:', price*(1-rate))
discount(10000)
discount(10000, 0.2)
discount(10000, rate=0.5)