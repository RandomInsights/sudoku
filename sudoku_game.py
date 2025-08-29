
class Sudoku:
    def __init__(self, board : list[list[int]]):
        self._board = board

    def get_board(self):
        return self._board.copy()
    
    def get_row(self, rowNum : int):
        return self.get_board()[rowNum]
    
    def get_col(self, colNum: int):
        col = []

        for row in self.get_board():
            col.append(row[colNum])
        
        return col
    
    def get_square(self, gridRowNum : int, gridColNum : int):
        square = []
        board = self.get_board()

        for i in range(3):
            for j in range(3):
                square.append(board[gridRowNum * 3 + i][gridColNum * 3 + j])

        return square
    
    def get_cell(self, rowNum : int, colNum : int):
        return self.get_board()[rowNum][colNum]
    
    def cell_pos_to_square_pos(self, rowNum : int, colNum : int):
        return ((rowNum // 3), (colNum // 3))
    
    def set_cell(self, rowNum : int, colNum : int, digit : int):
        self._board[rowNum][colNum] = digit

    def valid_seq(self, sequence : list[int]):
        presentDigits = []

        for digit in sequence:
            if digit != ' ':
                if digit in presentDigits or digit not in range(1, 10):
                    return False
                else:
                    presentDigits.append(digit)
        
        return True
    
    def valid_row(self, rowNum : int):
        return self.valid_seq(self.get_row(rowNum))
    
    def valid_col(self, colNum : int):
        return self.valid_seq(self.get_col(colNum))
    
    def valid_square(self, gridRowNum : int, gridColNum : int):
        return self.valid_seq(self.get_square(gridRowNum, gridColNum))
    
    def grid_full(self):
        for row in self.get_board():
            for digit in row:
                if digit == ' ':
                    return False
        
        return True
    
    def solved_grid(self):
        if not self.grid_full():
            return False
        
        for i in range(9):
            if not self.valid_row(i) or not self.valid_col(i):
                return False
        
        for i in range(3):
            for j in range(3):
                if not self.valid_square(i, j):
                    return False
        
        return True

    def __str__(self):
        boardStr = ""

        for i, row in enumerate(self.get_board()):
            for j, column in enumerate(row):
                boardStr += str(column)
                if j in (2, 5):
                    boardStr += '|'
            boardStr += '\n'
            if i in (2,5):
                boardStr += "---+---+---\n"
        
        return boardStr