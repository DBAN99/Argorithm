
# 2차원 리스트 초기화 시키는 방법

n = 4
m = 3

arr = [[0]* m for _ in range(n)]
print(arr)

# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Day 8 Dictionaries and Maps

n = int(input())
# N 값 만큼 반복해서 name_numbers에 값 리스트 형식으로 집어넣기
name_numbers = [input().split() for _ in range(n)]

phone_book = {k: v for k,v in name_numbers}

while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break