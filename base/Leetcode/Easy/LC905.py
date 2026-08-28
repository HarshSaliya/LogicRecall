class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] % 2 !=0 and nums[right] %2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                
                left +=1
                right -=1
            elif nums[left] % 2 == 0 and nums[right] % 2 ==0:
                left +=1
            else :
                right -=1
        
        return nums




# python using only
# nums = [3,1,2,4]

# res = []
# res2  = []
# for i in nums:
#     if i % 2 == 0:
#         res.append(i)
#     else:
#         res2.append(i)

# print(res+res2)


# --------- practice 
# # nums = [3,1,2,4]
# # nums = [0,1,2]
# nums =[0,2,1,4]
# # Output: [2,4,3,1]


# # nums = [1,3,4,6,7]

# left, right = 0, len(nums)-1

# # for i  in range(1, len(nums)):
# while left <= right:
#     print(f"Start of loop  LEFT :: {nums[left]} RIGHT :: {nums[right]}")
    
#     if nums[left] == 0:
#         left +=1
#         continue
#     if nums[left] % 2 !=0 and nums[right] %2 == 0:
#         print("If condiotn::")
#         nums[left], nums[right] = nums[right], nums[left]
        
#         left +=1
#         right -=1
#         print("Nums current list", nums)
#     elif nums[left] % 2 == 0 and nums[right] % 2 ==0:
#         left +=1
#     else :
#         right -=1
        
    
# print(nums)
    