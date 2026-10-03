class Solution(object):
    def isAnagram(self, s, t):
        seen = {}
        seen_2 = {}
        total = 1
        total2 = 1
        if len(s) == len(t):
            for i in range(len(s)):
                print(s[i])
                
                if s[i] in seen.keys():
                    seen[s[i]] += 1
                else:
                    seen[s[i]] = total
                    
                if t[i] in seen_2.keys():
                    seen_2[t[i]] += 1
                else:
                    seen_2[t[i]] = total2
        
            return seen == seen_2
        return False
