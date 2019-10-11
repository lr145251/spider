from search import swap

# 二分
def binary_sort(list1, key):
    L = 0
    R = len(list1)

    while L <= R:
        mid = L + ((R - L) >> 1)
        if list1[mid] < key:
            L = mid + 1
        elif list1[mid] > key:
            R = mid - 1
        else:
            return mid
    return -1

# 冒泡
def buddle_sort(list1):
    for end in range(len(list1) - 1, 0, -1):
        for i in range(0, end):
            if list1[i] > list1[i + 1]:
                swap(list1, i, i + 1)
    return list1


# 插排
def insert_sort(list1):
    for i in range(1, len(list1)):
        temp = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > temp:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = temp



# 快排
def quick_sort(list1,left,right):
    p = partition(list1,left,right,list1[right])
    quick_sort(list1,left,p[0]-1)
    quick_sort(list1,p[1]+1,right)

def partition(list1,left,right,key):
    less = left-1
    more = right+1
    cur = left
    while cur < more:
        if list1[cur] < key:
            swap(list1,less+1,cur)
            less += 1
            cur += 1
        elif list1[cur] > key:
            swap(list1,more-1,cur)
            more -= 1
        else:
            cur += 1
    return less+1 ,more-1




