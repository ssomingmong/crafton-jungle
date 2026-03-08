# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


arr = []
max = 0
count = 0
for i in range(9):
    arr.append(int(input()))

for i in arr:
    
    if i > max:
        max = i

for i in range(9):
    if max == arr[i]:
        count = i + 1
        break
print(max)
print(count)