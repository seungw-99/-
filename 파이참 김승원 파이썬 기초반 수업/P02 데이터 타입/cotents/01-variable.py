'''
#변수 (variable)
데이터를 저장하는 공간에 이름을 붙임

#변수 선언
   변수명 = 데이터

#변수명 작성규칙
1. 알파벳, 숫자, 언더바(_)로 구성
2. 대소문자 구분함 대문자A 소문자a 서로 별개의 언어로 취급함
3. 공백이나 특수기호 사용불가 언더바만 (_)만 가능
4. 숫자로 시작할 수 없음
5. 파이썬 명령어 사용불가 ex) for, break
'''
var1 = 10
var2 = 20
sum = var1 + var2
print(sum)

# 불가능한 변수명
#2someplace = 10 #twosomeplace = 10 숫자시작x
num = 10 #n um = 10 공백x
#abc@naver.com = 10 특수기호x
# for = 10 파이썬 명령어x

# 두 단어의 구분을 대문자 혹은 (_)로 연결 (변수는 소문자로 시작 두번째 단어 시작에서만 대문자), 상수는 전부 대문자로만 씀
rainySeason = 10
phone_num = '1111'
phone_Num = '2222'
print(phone_num)
print(phone_Num) #대소문자 구분함