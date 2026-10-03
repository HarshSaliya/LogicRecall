pattern = "abba"
s = "dog cat cat fish"
pattern = "abba"
s = "dog cat cat dog"
# new = s.split(" ")
# result = {}

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new = s.split(" ")
        result = {}
        print(new)
        if len(pattern) != len(new):
            return False


        for i in range(len(pattern)):
            if pattern[i] not in result.keys():
                if new[i] in result.values():
                    print("Failed")
                    return False
                result[pattern[i]] = new[i]
            elif result.get(pattern[i]) != new[i]:
                print("00000",result.get(pattern[i]))
                print("False")
                return False
                    
        print(result.get(pattern[i]), "lagse vaar pn aavse maja")    
        print("True")
        return True
        
Solution = Solution()
Solution.wordPattern(pattern=pattern, s=s)