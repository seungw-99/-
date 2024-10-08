'''
Q)  자연수를 입력 받아서 홀수인지 짝수인지 판별하여 출력하시오.

    ↓ 실행화면 ↓
   자연수를 입력하세요: 30
   짝수입니다.
'''
from unicodedata import numeric

num = int(input('자연수를 입력하세요: '))
if num%2==0:
    print('짝수입니다')
else:
    print('홀수입니다')