# s = "leetcode"
s = "loveleetcode"
# s = "aAbb"
# s ="loveleetcode"

class Solution(object):
    def firstUniqChar(self, s):
        res = 0
        for i in range(len(s)):
            seen = False
            for j in range(len(s)):
                # print(s[i],s[j])
                # print(i,j)
                if s[i] == s[j] and i != j:
                    seen =True
                    break

            if seen == False:
                # print("RESULT, ", s[i])
                return i
                # pass
                
        return -1


# Solution = Solution()
# print(Solution.firstUniqChar(s=s))
