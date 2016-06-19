import time
from random import shuffle

def merge_sort(arr):
    l = len(arr)
    if len(arr) < 2:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    out = []
    li = ri = 0  # pointer to next element from left, right halves
    while True:
        if li >= len(left):  # left half is exhausted
            out.extend(right[ri:])
            break
        if ri >= len(right): # right half is exhausted
            out.extend(left[li:])
            break
        if left[li] < right[ri]:
            out.append(left[li])
            li += 1
        else:
            out.append(right[ri])
            ri += 1
    return out

test = list(range(100000))
shuffle(test)
start = time.time()
merge_test = merge_sort(test)
merge_time = time.time() - start
print('merge sort: {} seconds'.format(round(merge_time, 5)))
start2 = time.time()
py_test = sorted(test)
py_time = time.time() - start2
print('Python sort: {} seconds'.format(round(py_time, 5)))
print('Ratio merge : Python sort:', round(merge_time/py_time, 4))
print('equal?', py_test == merge_test)
