# 搜尋法
from random import randrange
from time import time

r = randrange(10000000001)

def LinearSearch():
    
    startTime = time()
    
    for i in range(10000000001):
        if r == i:
            print('找到答案了，是' + str(i))
            print('線性搜尋法花了' + str(time() - startTime) + '秒')
            break

def BinarySearch():
    
    startTime = time()
    
    lower = 0
    upper = 100000000
    
    while lower <= upper:
        mid = (lower + upper) // 2
        
        if mid < r:
            lower = mid + 1
            
        elif mid > r:
            upper = mid - 1
            
        else:
            print('找到答案了，是' + str(mid))
            print('二元搜尋法花了' + str(time() - startTime) + '秒')
            return

LinearSearch()
BinarySearch()

