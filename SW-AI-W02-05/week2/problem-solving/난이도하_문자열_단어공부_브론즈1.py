# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

string = input().upper()
counts = {}

for i in string:
    counts[i] = counts.get(i, 0) + 1

max_value = max(counts.values())

result = []

for i in counts:
    if counts[i] == max_value:
        result.append(i)

if len(result) > 1:
    print("?")

else:
    print(result[0])




























# word = input().upper()

# counts = {}

# for ch in word:
#     counts[ch] = counts.get(ch, 0) + 1

# max_count = max(counts.values())

# result = []

# for ch in counts:
#     if counts[ch] == max_count:
#         result.append(ch)

# if len(result) > 1:
#     print("?")
# else:
#     print(result[0])