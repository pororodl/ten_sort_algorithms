############################################################
#python 可以快速的交换两个变量的值，是因为底层的c代码
#注意冒泡排序的两层循环i和j的取值
#key：相邻的相比较，大的换到后面去
############################################################
def BubbleSort(array):
    for i in range(len(array)):                             #表示换了几个数到后面去了
        for j in range(len(array)-i-1):                     # 要注意这里的-1
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]   # 把大的数换到后面去

if __name__ == '__main__':
    array = [2,4,1,4,7]
    BubbleSort(array)
    print(array)