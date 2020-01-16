def countingSort(arr, maxValue):      # 计数排序
    bucketLen = maxValue + 1

    bucket = [0] * bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    print(bucket)
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    # return arr


if __name__ == '__main__':
    arr = [2,3,4,7,3,5,6]
    maxValue = 7
    countingSort(arr,maxValue)
    print(arr)
