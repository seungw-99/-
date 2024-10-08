#== 문자열 관련 함수 ==#
happy = 'My Weekend'

# 문자열 길이 구하기
print(len(happy))

# 문자 개수 세기
print('e의 개수:', happy.count('e'))
print('e의 개수:', happy.count('ee'))

# 특정 문자 위치 찾기
print('y의 위치:', happy.index('y'))
print('y의 위치:', happy.find('y'))
# print('없는 문자 찾을 때:', happy.index('a'))
print('없는 문자 찾을 때:', happy.find('a'))
print()

# 공백 제거하기
s = ' fall '
print(f'원본: ({s})')
print(f'양옆 공백 제거: ({s.strip()})')
print(f'왼쪽 공백 제거: ({s.lstrip()})')
print(f'오른쪽 공백 제거: ({s.rstrip()})')

num ='95%'
print('%제거:', num.strip('%'))

stars ='**밤*하늘의별****'
print('양옆 *제거:', stars.strip('*'))
print()

# 문자열 바꾸기
s1 = 'It is summer'
s2 = s1.replace('summer', 'fall')
print(s2)
print(stars.replace('*', '')) # 문자열에서 특정 문자 제거
print()

# 문자열 나누기
a = 'Fall is coming'
k = a.split()
print(k) # 빈칸 기준으로 문자열들을 나누어서 리스트에 저장

phone = '010-1234-5678'
print(phone.split('-'))
print('핸드폰 뒷자리:', phone.split('-')[-1])

birth = '1999.09.09'
print('생년:', birth.split('.')[0])
print('이번 달 생일?', birth.split('.')[1] == '09')
