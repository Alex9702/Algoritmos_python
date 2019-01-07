import math

def merge(arr1, arr2):
    results = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j += 1

    while i < len(arr1):
        results.append(arr1[i])
        i += 1
    while j < len(arr2):
        results.append(arr2[j])
        j += 1
    return results

def merge_sort(arr):
    if len(arr) <= 1: 
        return arr

    mid = math.floor(len(arr)/2) 
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)  


# print(merge([100,200], [1,2,3,5,6])) 

print(merge_sort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]))