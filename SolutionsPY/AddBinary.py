class AddBinary:
    def addBinary(self, a, b):
        a= "1010"
        b="1011"
        resA=[]
        resB=[]
        reslist=[]
        for i in range(len(a)):
            resA.append(int(a[i]))
        for j in range(len(b)):
            resB.append(int(b[j]))
        m=1
        up=0
        temp=0
        while m<=max(len(resA),len(resB)):
            if m<=len(resA) and m<=len(resB):
                temp=resA[-m]+resB[-m]+up
                if temp==2:
                    up=1
                    temp=0
                elif temp==3:
                    up=1
                    temp=1
                else:
                    up=0
            elif m>len(resA):
                temp=resB[-m]+up
                if temp==2:
                    up=1
                    temp=0
                else :
                    up=0
            elif m>len(resB):
                temp=resA[-m]+up
                if temp==2:
                    up=1
                    temp=0
                else :
                    up=0
            reslist.insert(0,temp)
            m+=1
        if up!=0:
            reslist.insert(0,1)
        result="".join([str(x) for x in reslist])
        return result