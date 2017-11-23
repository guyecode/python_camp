# coding: utf-8
from copy import deepcopy

nums = range(2, 20)
for i in nums:
    nums = filter(lambda x: x == i or x % i, nums)
    print(i, list(deepcopy(nums)))
print(list(nums))