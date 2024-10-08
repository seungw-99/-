#== 출력문 옵션 알아보기 ==#
#separatot: (,)사이 출력할 데이터들을 sep= '내용'으로 연결

print('8월', '15일', '광복절') #sep= ' '이 기본값
print('8월', '15일', '광복절', sep='')
print('2024', '08', '15', sep= '-')
print('시험난이도: TOEFL', 'TOEIC', sep= '>>>\t')
print('12+34', 12+34, sep='=')
print()

#end: 문자열의 마지막을 end= '내용'으로 출력
#default값은 end='\n'
print('원주율:', 3.141, end='\n')
print(592)
print('asd99dd', end='@')
print('naver.com')
print()

#sep, end 함께 사용하기
print(8, 15, sep=' ', end='\n')
print(8+15)
print('8+15', 23, sep='=')