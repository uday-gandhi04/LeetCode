class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(index=0):
            if index == len(empties):
                return True

            i, j = empties[index]
            box_index = (i // 3) * 3 + j // 3
            
            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_index]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
                    
                    if backtrack(index + 1):
                        return True
                    
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)
                    board[i][j] = '.'
            
            return False

        backtrack()