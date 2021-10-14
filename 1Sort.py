

# 오름차순으로 정렬하는 프로그램 만들기
# 1 5 2 3 4 6 7 9 10 8

arr = [8,6,4,2,1,3,5,7,9,10]

def sort(arr):

    # arr라는 리스트의 크기를 n에 저장
    n = len(arr)
    # n번 반복문을 반복해서 실행시킨다. ex:) 10이면 0부터 9까지 총 10번
    for i in range(n):
        #min에 0부터 n-1을 집어 넣는다.
        min = i
        # j안에 i+1 부터 n번까지 집어 넣는다.
        for j in range(i+1, n):
            # 만약 arr[1]이 arr[0]보다 작다면 min에 j를 저장
            if arr[j] < arr[min]:
                min = j
        # arr[i]와 arr[min]값의 위치를 서로 바꿔준다.
        arr[i],arr[min]=arr[min],arr[i]
        print(arr)



print("before: ", arr)
sort(arr)
print("after: ", arr)
