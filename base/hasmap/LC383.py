class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        cnt = {}
        count =1

        for  i in magazine:
            print(i)
            if i not in cnt:
                cnt[i] =  count
            else:
                cnt[i] =  cnt.get(i, 0) + 1

        for j in ransomNote:
            if cnt.get(j, 0) <= 0:
                return False
            cnt[j] -= 1

        return True
