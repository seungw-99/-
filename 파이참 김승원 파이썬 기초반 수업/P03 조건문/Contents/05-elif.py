'''
# elif문 (else if)
조건식이 여러개인 경우 사용
elif문은 여러개 사용 가능

# if - elif - else
    if 조건식A:
        (조건식 A가 참이면 실행)
        실행문..
    elif 조건식 B:
        실행문..
    elif 조건식 C:
        실행문..
    ...
    else:
        실행문..
'''
movie = ''
if movie == '범죄도시':
    print('너 납치된거야')
elif movie == '타짜':
    print('사쿠라네!?')
elif movie == '베테랑':
    print('어이가 없네')
else:
    print('개설된 영화가 아닙니다')

# 예재) 점수에 따른 성적 등급 나타내보기
score = int(input('점수 입력: '))
if score>=90:
    print('A')
elif score>=80: #score<90:
    print('B')
elif score>=70: #score<80:
    print('c')
elif score >=60: #score < 70:
    print('D')
else:
    print('F')