# 插入排序
#key:把第一个元素当成一个已经排好了的序列，从第二个开始和前面已经排好的序列进行比较，倒（顺）着比较，选择合适的位置进行插入
def InserSort(array):
    for i in range(1,len(array)):
        for j in range(i,0):
            if array[i]<array[j]:


