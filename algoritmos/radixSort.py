import math

def get_digit(num, i):
    return math.floor(abs(num)/math.pow(10, i))%10

# def count_digits(num):
#     return math.floor(math.log10(abs(num))) + 1
#
# def get_max(nums):
#     maxDigit = 0
#     for num in nums:
#         maxDigit = max(max)
#     return maxDigit

def get_max(nums):
    return math.floor(abs(math.log10(max(nums)))) + 1

def radix_sort(nums):
    maxDigitCount = get_max(nums)
    for k in range(maxDigitCount):
        collectBucket = [[] for i in range(10)]
        for i in range(len(nums)):
            digit = get_digit(nums[i], k)
            collectBucket[digit].append(nums[i])
        nums = []
        for n in collectBucket:
            nums += n
    return nums

# lista = [23,345,5467,12,2345,9852]
lista = [3221, 1, 10, 9680, 577, 9420, 7, 5622, 4793, 2030, 3138, 82, 2599, 743, 4127]

print(radix_sort(lista))

