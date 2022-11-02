class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x is the base, 2
        n is the power, 3
        result is 2**3=8
        """

        if x==0 or x==1:
            print(1)
        else:
            # return myPow(x ** n)
            print(x**n)

p1= Solution()
p1.myPow(float(input("Enter number")), int(input("Enter power")))




