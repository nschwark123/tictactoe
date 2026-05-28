from game import Game
from player import Player

def menu():
    print("\n=== TIC TAC TOE ===")
    print("1. Spielen")
    print("2. Beenden")
    return input("Auswahl: ")

def main():
    while True:
        choice = menu()

        if choice == "1":
            name1 = input("Spieler 1: ") or "X"
            name2 = input("Spieler 2: ") or "O"

            p1 = Player(name1, "X")
            p2 = Player(name2, "O")

            game = Game(p1, p2)

            rounds = input("Runden (default 3): ")
            rounds = int(rounds) if rounds.isdigit() else 3

            for i in range(rounds):
                print(f"\n--- Runde {i+1} ---")
                game.play()

                print("\nScore:")
                print(p1.name, p1.score)
                print(p2.name, p2.score)

            print("\n=== Spiel Ende ===")
            if p1.score > p2.score:
                print(p1.name, "gewinnt gesamt!")
            elif p2.score > p1.score:
                print(p2.name, "gewinnt gesamt!")
            else:
                print("Unentschieden gesamt!")

        elif choice == "2":
            break
        else:
            print("Ungültig")

if __name__ == "__main__":
    main()