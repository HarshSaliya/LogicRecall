class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n >= 1:
            total = 0
            if n in seen:
                return False   
                # print("flase")
                # break
            seen.add(n)
            while n >0:
                num2  = n % 10
                # print("num2 :::::::", num2)
                total += num2 * num2
                n = n // 10
                # print("Second one ", n)
                # i -=1
            n = total
            print(n)

            if n == 1:
                return True
        return False
