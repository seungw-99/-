'''
Q)  3개의 점수를 입력 받고
    점수들의 평균값이 80점 이상이면 ‘합격’
    아니면 ‘불합격’을 출력하시오.

    ↓ 실행화면 ↓
   점수1 입력: 70
   점수2 입력: 80
   점수3 입력: 85
   시험 결과: 불합격
'''
score1 = int(input('점수1 입력: '))
score2 = int(input('점수2 입력: '))
score3 = int(input('점수3 입력: '))
if (score1+score2+score3)/3>=80:
    k = '합격'
else:
    k = '불합격'
    print('시험 결과:', k)