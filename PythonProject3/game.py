from board import Board

class Game:
    def __init__(self, p1, p2):
        self.board = Board()
        self.p1 = p1
        self.p2 = p2
        self.current = p1

    def switch(self):
        self.current = self.p2 if self.current == self.p1 else self.p1

    def play(self):
        self.board.reset()
        self.current = self.p1

        while True:
            self.board.display()

            try:
                move = int(input(f"{self.current.name} ({self.current.symbol}) 0-8: "))
            except:
                print("Ungültig")
                continue

            if move < 0 or move > 8:
                print("Nur 0-8 erlaubt")
                continue

            if not self.board.make_move(move, self.current.symbol):
                print("Feld belegt")
                continue

            if self.board.winner(self.current.symbol):
                self.board.display()
                print(self.current.name, "gewinnt!")
                self.current.score += 1
                return self.current

            if self.board.full():
                self.board.display()
                print("Unentschieden!")
                return None

            self.switch()