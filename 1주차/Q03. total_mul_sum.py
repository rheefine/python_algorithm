"""
-----------------  Question  -----------------
10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
10 = 1 * 0 = 0
11 = 1 * 1 = 1
12 = 1 * 2 = 2
13 = 1 * 3 = 3
14 = 1 * 4 = 4
15 = 1 * 5 = 5
그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15
----------------------------------------------
"""
# 과제 1. 10~15까지의 숫자를 분해하여 곱하기의 전체 합을 구하시오(1). 
## 출력 : 15

c = 0

for i in range(10, 16):
    a = list(str(i))

    b = int(a[0])*int(a[1])

    c += b

print (c)


#--------------------------------------------------------------------------------------------------------------


# 과제 2. 10~1000까지의 숫자를 분해하여 곱하기의 전체 합을 구하시오(2).
## 출력 : 93150

c = 0

for i in range(10, 1000):
    a = list(str(i))

    b =1
    for j in range(len(a)):
        b *= int(a[j])

    c += b

print (c)

