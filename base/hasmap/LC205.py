class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}

        for i in range(len(s)):
            if s[i] not in dic.keys():
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
            elif dic.get(s[i]) != t[i]:
                return False

        return True