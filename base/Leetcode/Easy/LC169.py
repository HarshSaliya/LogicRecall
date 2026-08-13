from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1

        value = max(dic.values())
        # print("maxx ::", value)
        for k, v in dic.items():

            if value == v:
                # print("final",v)
                return k
                break

nums = [3,2,3]
s = Solution()
print(s.majorityElement(nums))
