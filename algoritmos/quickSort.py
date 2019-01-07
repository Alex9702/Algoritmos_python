def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

def pivot(arr, start, end):
    pivot = arr[start]
    swapIdx = start

    for i in range(start + 1, end):
        if pivot > arr[i]:
            swapIdx += 1
            swap(arr, swapIdx, i)
    swap(arr, start, swapIdx)
    return swapIdx

def quick_sort_helper(arr, left, right):
    if(left >= right): return arr
    pivotIdx = pivot(arr, left, right + 1)
    quick_sort_helper(arr, left, pivotIdx - 1)
    quick_sort_helper(arr, pivotIdx + 1, right)

def quick_sort(arr):
    left = 0
    right = len(arr) - 1
    quick_sort_helper(arr, left, right)
    return arr

lista = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
# lista = [5,2,1,8,4,7,6,3]
# lista = [ 7, 6, 8]
print(quick_sort(lista))
