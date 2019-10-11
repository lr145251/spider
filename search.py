# import threading
#
#
def swap(list1, x, y):
    list1[x], list1[y] = list1[y], list1[x]

#
# def buddle_sort(list1):
#     for end in range(len(list1) - 1, 0, -1):
#         for i in range(0, end):
#             if list1[i] > list1[i + 1]:
#                 swap(list1, i, i + 1)
#
#     return list1
#
#
# def insert_sort(list1):
#     for i in range(1, len(list1)):
#         temp = list1[i]
#         j = i - 1
#
#         while j >= 0 and list1[j] > temp:
#             list1[j + 1] = list1[j]
#             j -= 1
#
#         list1[j + 1] = temp
#
#     return list1
#
#
# def binary_sort(list1, k):
#     L = 0
#     R = len(list1)
#
#     while L <= R:
#         mid = L + ((R - L) >> 1)
#
#         if list1[mid] > k:
#             R = mid - 1
#         elif list1[mid] < k:
#             L = mid + 1
#
#         else:
#             return mid
#     return -1
#
#
# class SingleInstance():
#     instance = None
#
#     def synch(func):
#         func.lock = threading.Lock()
#
#         def lock_func(*args, **kwargs):
#             with func.lock:
#                 return func(*args, **kwargs)
#
#         return lock_func
#
#     @synch
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = super().__init__(cls)
#         return cls.instance
#


#
# def partition(list1, left, right, key):
#     less = left - 1
#     more = right + 1
#     cur = left
#     while cur < more:
#         if list1[cur] < key:
#             swap(list1, less + 1, cur)
#             less += 1
#             cur += 1
#
#         elif list1[cur] > key:
#             swap(list1,more - 1,cur)
#             more -= 1
#
#         else:
#             cur += 1
#     return less + 1, more - 1
#
# def quick_sort(list1,left,right):
#
#     if left < right:
#         p = partition(list1,left,right,list1[right])
#
#         quick_sort(list1,left,p[0]-1)
#
#         quick_sort(list1,p[1] + 1,right)
#
#
# list1 = [2,1,4,5,8,1,7,6,3]
# quick_sort(list1,0,len(list1)-1)
# print(list1)
#






















def partition(list1,left,right,key):
    less = left -1
    more = right +1
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


def quick_sort(list1,left,right):

    if left < right:
        p = partition(list1,left,right,list1[right])

        quick_sort(list1,left,p[0]-1)
        quick_sort(list1,p[1]+1,right)


list1 = [2,1,8,6,2,3,7,9]
quick_sort(list1,0,len(list1)-1)
print(list1)

