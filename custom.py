import heapq
from typing import List

def heapsort(arr: List[int]):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def quicksort(arr: List[int]):
    def Lomuto(a, low, high):
        pivot = a[high] # chọn pivot ngây thơ, lí do có time spike ở data đã sort
        i = low
        for j in range(low, high):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[high] = a[high], a[i]
        return i

    def _quicksort(a, low, high):
        if low < high:
            p = Lomuto(a, low, high)
            _quicksort(a, low, p - 1)
            _quicksort(a, p + 1, high)

    _quicksort(arr, 0, len(arr) - 1)
    return arr

def mergesort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l = mergesort(arr[:mid])
    r = mergesort(arr[mid:])
    return merge(l, r)
