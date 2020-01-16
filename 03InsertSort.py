# 插入排序
#key:把第一个元素当成一个已经排好了的序列，从第二个开始和前面已经排好的序列进行比较，倒（顺）(如果是升序就需要从前往后比较，降序就是从后往前比较）着比较，选择合适的位置进行插入,并且要把后面的数字右移
def InserSort(array):
    for i in range(1,len(array)):   #
        for j in range(0,i):
            if array[i]<array[j]:
                temp = array[i]
                for k in range(i,j-1,-1):
                    array[k]=array[k-1]
                array[j]=temp

if __name__ == '__main__':
     # nums=[23, 43, 0, 8, 11, 18]
    nums =[8, 7, 6, 12, 14, 13, 2, 1]
    InserSort(nums)
    print(nums)