class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 

        for idx, i in enumerate(nums):
            exist = target - i
            if exist in seen.keys():
                return [seen[exist], idx]
            else:
                seen[i] = idx



#  local 
# nums = [2,7,11,15]
# target = 17

# print("index find::", nums.index(2))
# seen = {}

# for i in nums:
#     # print(i)
#     exist = target - i
#     # print("Exist :::::", exist)
#     if exist in seen.keys():
#         print("Result ::::", exist, i)
#         print(nums.index(exist), nums.index(i))
#     else:
#         seen[i]= 0
