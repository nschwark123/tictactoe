class Board:
    def __init__(self):
        self.board = [" "] * 9

    def display(self):
        print()
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print(" | ".join(row))
            if i < 2:
                print("--+---+--")
        print()

    def make_move(self, i, symbol):
        if self.board[i] == " ":
            self.board[i] = symbol
            return True
        return False

    def reset(self):
        self.board = [" "] * 9

    def full(self):
        return " " not in self.board

    def winner(self, s):
        win = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        return any(all(self.board[i] == s for i in c) for c in win)