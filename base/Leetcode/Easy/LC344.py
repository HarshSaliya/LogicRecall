# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["h","e","l","l","o"]

class Solution(object):
    def reverseString(self, s):
        new = []
        # print(s[::-1])

        left, right =0, len(s)-1
        
        while left < right:
            s[left], s[right]= s[right], s[left]
            
            left +=1
            right -=1

        return s
    
    
s1= Solution()
print(s1.reverseString(s= ["h","e","l","l","o"]))



#  solve with new list craete
# new = []
# # print(s[::-1])

# for i in range(len(s) -1, -1, -1):
#     print(i)
    
#     new.append(s[i])


# print(new)