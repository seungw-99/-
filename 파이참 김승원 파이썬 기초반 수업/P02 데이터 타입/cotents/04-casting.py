'''
#타입 변환(Type Casting)
(타입 변환 = 캐스팅 = 형변환
    변환할타입(데이터)
'''
# 정수형 <- 실수형
num1 = int(3.14)
print('실수를 정수로 변환:', num1, type(num1))

# 실수형 <- 정수형
num2 = float(10)
print('정수를 실수로 변환:', num2, type(num2))

# 문자열 <- 정수형
msg = str(16)
print('정수를 문자열로 변환:', msg, type(msg))

# (에러)정수형 <- 문자열
# num0 = int('투썸플레이스')
# print(num0)

# 정수형 <- 문자열
num3 = int('402')
print('문자열을 정수로 변환:', num3, type(num3))
print()

# 정수와 실수, 문자열
a = 10 #int
b = 25.0 #float
c = '100' #str

# a+b
print(a+b) #정수+실수 => 실수
print(a+int(b))
print(str(a)+str(b)) #문자열 끼리 이어 붙임
print()

# b+c
# print(b+c)
print(b+int(c))
print(int(int(c)/b))