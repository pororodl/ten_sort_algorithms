#选择排序
#key:选择最小的放到第一个位置，选择第二小的放到第二个位置
def SelectedSort(array):
    for i in range(len(array)-1):   # 表示要进行多少次排序
        min = i
        for j in range(i+1,len(array)):
            if array[j]<array[min]:
                min = j
        array[i],array[min]=array[min],array[i]

if __name__ == '__main__':
    array = [2, 4, 1, 4, 7,3,10,1,1]
    SelectedSort(array)
    print(array)
