

# 오름차순으로 정렬하는 프로그램 만들기
# 1 5 2 3 4 6 7 9 10 8

arr = [8,6,4,2,1,3,5,7,9,10]

def sort(arr):

    n = len(arr)
    for i in range(n):
        min = i

        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]
        print(arr[:i+1])
print("before: ", arr)
sort(arr)
print("after: ", arr)
