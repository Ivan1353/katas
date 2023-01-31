class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps=0
        while num!=0:
            steps+=1
            if num%2 == 0:
                num /= 2
                print(num)
            else:
                num -= 1
                print(num)
        return steps
