# 백준 2562번
k = []
for i in range(9):
    num = int(input())
    k.append(num)

# 반복문
# max = 0
# max_idx = -1
# for i in range(9):
#     if k[i] > max:
#         max = k[i]
#         max_idx = i
# print(max)
# print(max_idx+1)

# 2. 파이썬 함수
print(max(k))
print(k.index(max(k))+1)