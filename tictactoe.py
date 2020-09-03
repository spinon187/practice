class Solution:
    def tictactoe(self, moves):
        b = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        def check(board):
            if board[0][0] == board[0][1] == board[0][2]:
                return True
            if board[0][0] == board[1][1] == board[2][2]:
                return True
            if board[0][0] == board[1][0] == board[2][0]:
                return True
            if board[0][1] == board[1][1] == board[2][1]:
                return True
            if board[0][2] == board[1][2] == board[2][2]:
                return True
            if board[1][0] == board[1][1] == board[1][2]:
                return True
            if board[2][0] == board[2][1] == board[2][2]:
                return True
            if board[2][0] == board[1][1] == board[0][2]:
                return True
        turn = 0
        for move in moves:
            active = 'B' if turn % 2 else 'A'
            b[move[0]][move[1]] = active
            if check(b):
                return active
            turn += 1
        return 'Draw' if len(moves) == 9 else 'Pending'