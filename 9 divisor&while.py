# a,b =map(int,input().split())
# c = []
# for i in range(1,a):
#     if a % i == 0:
#         c.append(i)
#
# if b > len(c):
#     print(0)
# else:
#     print(c[b-1])
#
# a = int(input())
# num = a
# cnt = 0
# # ---------------------------------
# while True:
#     b = num // 10 # 2
#     c = num % 10  # 6
#     d = (b + c) % 10  # 8
#     num = (c * 10) + d
#     cnt +=1
#
#     if num == a:
#         break
# print(cnt)

li = [5,2,3,1,4]
li.sort()
print(li)