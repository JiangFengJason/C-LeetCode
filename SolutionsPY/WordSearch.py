class WordSear:
    directList=[(0,-1),(0,1),(-1,0),(1,0)]
    def exist(self, board, word):
        m=len(board)
        if m==0:
            return False
        n=len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.search(board,marked,0,i,j,m,n,word):
                    return True
        return False
    
    def search(self,board,marked,index,start_x,start_y,m,n,word):
        if index==len(word)-1:
            return board[start_x][start_y]==word[index]

        if board[start_x][start_y]==word[index]:
            marked[start_x][start_y]=True
            for direct in self.directList:
                next_x=start_x+direct[0]
                next_y=start_y+direct[1]
                if 0<=next_x<m and 0<=next_y<n and not marked[next_x][next_y] and self.search(board,marked,index+1,next_x,next_y,m,n,word) :
                    return True
            marked[start_x][start_y]=False
        return False