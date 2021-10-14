arr = [5,2,3,1,4]
n = len(arr)

# 리스트의 크기  n-1부터 0까지 반복함
for i in range(n-1,0,-1):
    #n-1만큼 j를 반복함
    for j in range(i):
        # arr[0]과 arr[1]을 제일 먼저 비교해 arr[0]이 클 경우 arr의 위치 변경
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        print(arr)