# n = 2230
#
# count = 0
# coin_types = [500, 100, 50, 10]
#
# for coin in coin_types:
#     # 리스트 하나씩 뽑아서 n과 나눈 값을 count에 저장
#     count += n // coin
#     n %= coin
#
# print(count)



n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

answer = first * k * (m // k) + second * (m % k)
print(answer)