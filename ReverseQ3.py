class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else +1 # Keep the sign
        strx_rev = str(abs(x)) [::-1] # reverse the value
        max_limit = '2147483648' # This is 2^31
        if len(strx_rev)<10:  # If the number has less than 10 digit, it's acceptable
            return sign*int(strx_rev)
        if len(strx_rev)==10 and strx_rev<max_limit: # If the number has 10 digits, we need to make sure it's within boundries
            return sign*int(strx_rev)
        else:   # This case shouln't happen
            return 0