# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left =0
#         right =1

#         for i in range(1, len(nums)):
#             # print("same value", nums[left], nums[right])
            
#             if nums[left] != nums[right]:
#                 # print("Not same value", nums[left], nums[right])
#                 left +=1
#                 nums[left], nums[right]= nums[right], nums[left]
                
            
#             right +=1
#         print("The value of left",left+1)
#         return left +1



# nums  = [0,0,1,1,1,2,2,3,3,4]

# left =0
# right =1

# for i in range(1, len(nums)):
#     # print("same value", nums[left], nums[right])
    
#     if nums[left] != nums[right]:
#         # print("Not same value", nums[left], nums[right])
#         left +=1
#         nums[left], nums[right]= nums[right], nums[left]
        
#     right +=1  
        
# print(nums)

