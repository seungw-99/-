'''
Q)  물건의 금액을 입력 받아
    할인율에 따른 할인 금액을 구하시오.
    5000원 이상은 5%
    10000원 이상은 10%
    50000원 이상은 20%

    ↓ 실행화면1 ↓
   가격 입력: 8000
   할인금액: 400

    ↓ 실행화면2 ↓
   가격 입력: 20000
   할인금액: 2000

    ↓ 실행화면3 ↓
    가격 입력: 60000
   할인금액: 12000

    ↓ 실행화면4 ↓
    가격 입력: 3000
   할인금액: 0
'''
price = int(input('가격 입력: '))
rate = 0 #할인율

if price>=50000:
    rate = 0.2
elif price>=10000:
    rate = 0.1
elif price>=5000:
    rate = 0.05
else:
    rate = 0
print('할인금액:', int(price*rate))