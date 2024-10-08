'''
Q)   이중for문을 이용하여 아래의 형태처럼 결과를 출력해보시오.
   단, 같은 줄의 숫자 간의 공백 거리는 tab만큼이다.

   ↓ Console ↓
   1   2   3   4   5
   6   7   8   9   10
   11   12   13   14   15
   16   17   18   19   20
   21   22   23   24   25

   Tip) 탭만큼의 공백을 주는 코드는 "\t"
'''
for i in range(1, 6):
    for j in range(1, 6):
        print(5*(i-1)+j, end='\t')
    print()
print()

num = 1
for i in range(1, 6):
    for j in range(1, 6):
        print(num, end='\t')
        num+=1
    print()