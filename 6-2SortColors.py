# 이친구들을 000, 111 , 222 이러한 형식으로 만들어라
li = [1,0,2,2,0,1,2,1,0]

a = len(li)
left = 0
mid = 0
right = a-1
# mid라는 포인터가 right 크기보다 작거나 같을 때 계속 반복해준다.
while mid <= right:
    #mid는 0을 찾아서 왼쪽으로 보내준다
    if li[mid] == 0:
        li[left],li[mid] = li[mid],li[left]
        left+=1
        mid+=1
    #right는 2를 찾아서 오른쪽으로 보내준다.
    elif li[mid] == 2:
        li[right],li[mid]=li[mid],li[right]
        right-=1
    else:
        mid +=1
        
print(li)