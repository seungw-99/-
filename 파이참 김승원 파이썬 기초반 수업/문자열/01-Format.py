#== 문자열 포맷팅 ==#
# '{}'.format(): 포맷 함수를 사용한 포맷팅
print('사과 {}개 주세요'.format(3))
num = 5
print('자두 {}개 주세요'.format(num))
print('지불하실 {}은 총 {}{}입니다'.format('금액', '$', 30))
print('내가 {0} 기린 {1}은'
      '너가 {0} 기린 {1}보다 잘 그렸다'.format('그린', '그림'))
print('제 별명은 {nickname}이며 {age}세 입니다'
      .format(age=10, nickname='너구리'))
msg = '영화값이 너무 {}요'.format('비싸')
print(msg)
print('='*30)

#f'{}' : f문자열 포맷팅
seaeon = '가을'
print(f'다음 계절은 {seaeon}입니다')

a = 10
b = 20
print(f'{a} + {b} = {a+b}')

pi = 3.141592
print(f'{pi:03f}') #소수점 자리 표현

won = 1200000
print(f'{won:,}원') #천단위 콤마 표현

num = 0.9576
print(f'{num:0.2%}') #백분율 표현 {num:.2%} 넣어도 같음
print('='*30)

# %서식 문자를 사용한 포맷팅
print('오늘은 %d일 입니다' %28.5) # %d: 정수
print('오늘은 %d년 %d월 입니다' %(2024, 8))
print('체온은 %f도 입니다' %36.5) # %f: 실수
print('%.1f' %36.5) # %.표현자리수f
print('다음 계절은 %s 입니다' %'여름') # %s: 문자열
print('이니셜은 %c입니다' % 'D') # %c: 단일 문자

birth = (2004, '8', 28)
print('생년월일: %d년 %s월 %d일' %birth)

# print('생년월일: {}년 {}월 {}일'. format(birth, 0, 0)) 안됨