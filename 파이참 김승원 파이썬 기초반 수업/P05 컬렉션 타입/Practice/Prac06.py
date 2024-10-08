'''
Q)  반복문을 사용하여 다음 리스트 값들 중에서
    최대값과 최소값을 찾고 평균값을 구하시오.

    ↓ 실행화면 ↓
    최대값: 85
    최소값: 3
    평균값: 42.875
'''
k = [20, 55, 10, 3, 85, 36, 70, 64]
max = k[0]
min = k[0]
sum = 0
for num in k:
    if num > max:
        max = num
    if num < min:
        min = num
    sum += num
print('최대값:', max)
print('최소값:', min)
print('평균값:', sum/len(k))