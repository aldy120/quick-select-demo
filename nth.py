import math

def find_half_from(n):
    return (math.floor((n - 1)/2), math.ceil((n - 1)/2))

def slow_select(k, arr):
    return sorted(arr)[k]

def slow_find_median(arr):
    (a, b) = find_half_from(len(arr))
    return (slow_select(a, arr) + slow_select(b, arr))/2

def trivial_pick_pivot(arr):
    return arr[0]

def quick_select(k, arr, pivot_function = trivial_pick_pivot):
    pivot = pivot_function(arr)    
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    left = [x for x in arr if x < pivot]
    if k < len(left):
        return quick_select(k, left)
    if k < len(left) + len (mid):
        return pivot
    if k >= len(left) + len (mid):
        return quick_select(k - (len(left) + len(mid)), right)
    
def median_of_medians(arr):
    if len(arr) <= 5:
        return slow_find_median(arr)
    chunks = chunked(arr, 5)
    medians = [sorted(chunk)[2] for chunk in chunks if len(chunk) == 5]
    return median_of_medians(medians)

def chunked(arr, size):
    return [arr[i : i + size] for i in range(0, len(arr), size)]

def quick_find_median(arr):
    (a, b) = find_half_from(len(arr))
    return (quick_select(a, arr, median_of_medians) + quick_select(b, arr, median_of_medians))/2