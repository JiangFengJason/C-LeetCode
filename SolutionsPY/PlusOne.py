import math

class PlusOne:
    def plusOne(self, digits):
        sum=0
        res=[]
        for i in range(len(digits)):
            sum=sum+digits[i]*pow(10,(len(digits)-i-1))
        sum+=1
        for i in range(len(str(sum))):
            res.append(int(str(sum)[i]))
        return res