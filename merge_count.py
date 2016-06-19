# Merge sort that counts number of inversions in input array

def merge_count(arr):
    l = len(arr)
    if len(arr) < 2:
        return arr, 0
    half = len(arr) // 2
    left, count1 = merge_count(arr[:half])
    right, count2 = merge_count(arr[half:])
    count = count1 + count2
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
            count += len(left) - li
            ri += 1
    return out, count


arr = []
with open('array.txt', 'r') as f:
    for line in f:
        arr.append(int(line))

sortd, count = merge_count(arr)
print(count)