class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                print("duplicate found")
                return True
                break
        
        return False

nums  = [1,1,1,3,3,4,3,2,4,2]
s1= Solution()
print(s1.containsDuplicate(nums=nums))