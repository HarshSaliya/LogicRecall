class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        second = 0
        matched = 0

        if not s:
            return False

        for i in range(len(t)):
            # print(i)
            if s[first] == t[second]:
                # print("Matched", s[first], t[second])
                first +=1
                second +=1
                matched +=1
            else:
                second +=1
                # print("Not matched")
                

        if matched == len(s):
            # print(True)
            return True
        else:
            return False
        
s = ""
t = "ahbgdc"

s1 = Solution()
s1.isSubsequence(s=s, t=t)