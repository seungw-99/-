'''
#입력문: input()
저장받을 변수 input('입력멘트')
input()은 Run창에서 사용자로부터 내용을 입력 받아 문자열로 저장한다
'''
# print('입력하세요:', end='')
# a = input()
a = input('입력하세요: ') # 위 두줄과 동일
print('a =', a)

weather = input('오늘 날씨가 어떻습니까? ')
print('오늘 날씨는', weather)
print()

# 2번 입력 받고 출력하기
id = input('생성할 아이디: ')
pw = input('생성할 패스워드: ')
print(id, '님의 패스워드는', pw, '로 생성되었습니다.')