
class Sudoku:
    def __init__(self, board : list[list[int]]):
        self._board = board

    def get_board(self):
        return self._board.copy()
    
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
            
if __name__ == "__main__":
    board = [[1,2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9,1], [3,4,5,6,7,8,9,1,2], [1,2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9,1], [3,4,5,6,7,8,9,1,2], [1,2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9,1], [3,4,5,6,7,8,9,1,2]]
    test = Sudoku(board)

    print(test)