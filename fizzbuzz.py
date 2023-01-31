class Solution:
    def fizzBuzz(self, n: int):
        list1 = list(range(1,n+1))
        for i in list1:
            if i % 3 == 0 and i%5 == 0:
                list1[list1.index(i)] = "FizzBuzz"
            elif i % 3 == 0:
                list1[list1.index(i)] = "Fizz"
            elif i % 5 == 0:
                list1[list1.index(i)] = "Buzz"
        return list(map(str, list1))