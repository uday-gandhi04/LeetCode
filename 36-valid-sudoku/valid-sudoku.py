class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row=[]
        col=[]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.' and board[i][j] in row:
                    return False
                elif board[i][j]!='.':
                    row.append(board[i][j])
                if board[j][i]!='.' and board[j][i] in col:
                    return False
                elif board[j][i]!='.':
                    col.append(board[j][i])
            row=[]
            col=[]
    

        for i in range(9):
            box=[]
            if (0<=i<3):
                row=0
            elif(3<=i<6):
                row=3
            else:
                row=6
            
            if(i== 0 or i==3 or i==6 ):
                col=0
            elif(i==1 or i==4 or i==7):
                col=3
            else :
                col =6

            for j in range(row,row+3):
                for k in range(col,col+3):
                    if board[j][k]!='.' and board[j][k] in box:
                        return False
                    else:
                        box.append(board[j][k])

        
        return True
        
        

        