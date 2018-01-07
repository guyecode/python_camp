# coding: utf-8
from copy import deepcopy

nums = range(2, 20)
print(id(nums))
for i in nums:
    print('pre', i, list(deepcopy(nums)), id(nums))
    nums = filter(lambda x: x == i or x % i, nums)
    print('post', i, list(deepcopy(nums)), id(nums))
print(list(nums), id(nums))