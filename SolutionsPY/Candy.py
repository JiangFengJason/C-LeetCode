class Can:
    def candy(self, ratings):
        record=[1]*len(ratings)
        sum=0
        for i in range(len(ratings)-1):
            if ratings[i]<ratings[i+1] and record[i]>=record[i+1]:
                record[i+1]=record[i]+1
        for i in range(1,len(ratings)):
            if ratings[-i]<ratings[-(i+1)] and record[-i]>=record[-(i+1)]:
                record[-(i+1)]=record[-i]+1
        for child in record:
            sum+=child
        return sum