def onequickSort(nums,low,high):
    temp = nums[low]
    while low<high:
        while low<high and nums[high]>=temp:
            high-=1
        nums[low]=nums[high]
        while low<high and nums[low]<=temp:
            low+=1
        nums[high]=nums[low]
    nums[low]=temp
    return low

def QuickSort(nums,low,high):
    if low<high:
        index = onequickSort(nums,low,high)
        QuickSort(nums,low,index-1)
        QuickSort(nums,index+1,high)

def KMinth(nums,k):  # 找到第K小的数字K=[1,2,,,,len(nums)
    low = 0
    high = len(nums)-1
    k = k-1                        # 转换为索引
    index = onequickSort(nums, low, high)
    if k == index:
        return nums[index]

    while index!=k:
        if index<k:
            low = index+1
            # k-=k-low+1
        if index>k:
            high = index-1
        index = onequickSort(nums, low, high)

    return nums[index]

def KMaxth(nums,k):
    high = len(nums)-1
    k = high-k+1
    return KMinth(nums,k)

if __name__ == '__main__':
    nums = [8,7,6,12,14,13,2,1]
    # nums = [23,43,0,8,11,18]
    # nums = [2,1]
    # nums = [5,4,3,2,1]

    # QuickSort(nums,0,len(nums)-1)\
    # KMinth(nums,1)
    print(KMinth(nums,3))
    print(KMaxth(nums,7-3+1))
    print(nums)