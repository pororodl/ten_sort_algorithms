import math
def buildMaxHeap(arr):
    for i in range(math.floor(len(arr)/ 2)-1, -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    print(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1       # 保证不和已经排好序的进行调整
        heapify(arr, 0)
    return arr

def KMaxth(arr,k):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,len(arr)-k,-1):
        swap(arr, 0, i)
        arrLen -= 1  # 保证不和已经排好序的进行调整
        heapify(arr, 0)
    return arr[0]

if __name__ == '__main__':
    arr = [8,7,6,12,14,13,2,1]
    # heapSort(arr)
    res = KMaxth(arr,5)
    print(arr)
    print(res)
