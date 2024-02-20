import copy
def solution(arr):
    x = 0
    arr1 = []
    while arr1 != arr:
        arr1 = copy.deepcopy(arr)
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i]*2 + 1
        x += 1
    return x - 1