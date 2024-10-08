'''
#중첩 조건문
if문 안에 새로운 if문을 추가
'''
age = 15
cm = 160

# 중첩 조건문
if age>=14:
    if cm>=160:
        print('번지점프 가능')
    elif cm>=170:
        print('롤러코스터 가능')
    else:
        print('후룸라이드 가능')
else:
    print('회전목마 올라가자')

# 논리연산자를 사용한 조건문
if age>=14 and cm>=160:
    print('번지점프 가능')
elif age>=14 and cm>=140:
    print('롤러코스터 가능')
elif age>=14:
    print('후룸라이드 가능')
else:
    print('회전목마 올라가자')
