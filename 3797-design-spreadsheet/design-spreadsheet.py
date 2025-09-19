class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.sheet=[[0 for _ in range(rows+1)] for _ in range(26) ]
        

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        i,j=ord(cell[0])-ord('A'),int(cell[1:])
        self.sheet[i][j]=value
        

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        i,j=ord(cell[0])-ord('A'),int(cell[1:])
        self.sheet[i][j]=0
        

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        i=formula.index('+')
        X=formula[1:i]
        Y=formula[i+1:]

        if ord('A')<=ord(X[0])<=ord('Z'):
            i,j=ord(X[0])-ord('A'),int(X[1:])
            xval=self.sheet[i][j]
        else:
            xval=int(X)
        
        if ord('A')<=ord(Y[0])<=ord('Z'):
            i,j=ord(Y[0])-ord('A'),int(Y[1:])
            yval=self.sheet[i][j]
        else:
            yval=int(Y)
        

        return xval+yval

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)