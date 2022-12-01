"""
-----------------  Question  -----------------
피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?
----------------------------------------------
"""
# 과제 1. 피보나치 수열을 만들면서, 동시에 계산을 수행하세요.
## 출력 : 4613732

aList = [1,2]

for i in range(0,100):
    
    aList.append(aList[i]+aList[i+1])

    if aList[i+2]>4000000:
        del(aList[i+2])
        break

print(aList)

for j in range(0,i+2):
    print(j)
    if aList[j]%2 == 1:
        aList[j]=0

print(aList)
print(sum(aList))