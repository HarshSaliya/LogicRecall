# Input: s = "abc", t = "ahbgdc"
# Output: true


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        second = 0
        matched = 0

        if not s:
            return True

        for i in range(len(t)):
            if first == len(s):
                break
            if s[first] == t[second]:
                first += 1
                second += 1
                matched += 1
            else:
                second += 1

        if matched == len(s):
            return True
        else:
            return False


#  Practice

# s = "abc"
# t = "ahbgdc"

# s = ""
# t = "ahbgdc"

# first = 0
# second = 0

# matched = 0

# for i in range(len(t)):
#     # print(i)


#     if s[first] == t[second]:
#         # print("Matched", s[first], t[second])
#         first +=1
#         second +=1
#         matched +=1
#     else:
#         second +=1
#         # print("Not matched")


# if matched == len(s):
#     print(True)
# else:
#     print(False)
