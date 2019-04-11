class divideTwo:
    def divide(self, dividend: int, divisor: int) -> int:
        # positive=(dividend>0) is (divisor>0)
        # dividend,divisor=abs(dividend),abs(divisor)
        # res=0
        # while dividend>=divisor:
        #     temp,i=divisor,1
        #     while dividend>temp:
        #         dividend-=temp
        #         res+=i
        #         i=i<<1
        #         temp=temp<<1
        # if not positive:
        #     res=-res
        # return min(max(-2147483648,res), 2147483647)
        neg = (dividend >= 0) ^ (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)

        pos, base = 1, divisor 
        while base <= dividend:
            pos <<= 1
            base <<= 1

        base >>= 1
        pos >>= 1

        res = 0
        while pos > 0:
            if base <= dividend:
                res += pos
                dividend -= base
            base >>= 1
            pos >>= 1
        val = -res if neg else res
        return 2 ** 31 -1 if val > 2 ** 31 -1 else val