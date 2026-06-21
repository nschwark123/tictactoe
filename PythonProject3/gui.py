import tkinter as tk
# → Import der GUI-Bibliothek

root = tk.Tk()
# → Erstellt Hauptfenster der App

root.title("Tic Tac Toe")
# → Setzt den Fenstertitel

current = "X"
# → Speichert, welcher Spieler gerade dran ist

board = [" "] * 9
# → Spielbrett mit 9 Feldern (leer am Anfang)

buttons = []
# → Hier speichern wir alle 9 Buttons (Spielfelder)


def click(i):
    global current
    # → sagt: wir verändern die globale Spieler-Variable

    if board[i] != " ":
        return
    # → verhindert, dass ein Feld zweimal geklickt wird

    board[i] = current
    # → setzt X oder O ins Spielfeld

    buttons[i].config(text=current, state="disabled")
    # → zeigt das Zeichen im Button und sperrt ihn

    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    # → alle möglichen Gewinnkombinationen

    for a,b,c in wins:
        if board[a] == board[b] == board[c] == current:
            result.config(text=current + " gewinnt!")
            disable()
            return
    # → wenn 3 gleiche Zeichen in einer Linie sind → Sieg

    if " " not in board:
        result.config(text="Unentschieden!")
        return
    # → wenn kein Feld mehr frei ist → Unentschieden

    current = "O" if current == "X" else "X"
    # → Spielerwechsel

    turn.config(text="Am Zug: " + current)
    # → Anzeige aktualisieren


def disable():
    # → sperrt alle Buttons nach Spielende
    for b in buttons:
        b.config(state="disabled")


def reset():
    global current, board
    # → setzt Spiel komplett zurück

    current = "X"
    board = [" "] * 9
    # → Spieler und Spielfeld zurücksetzen

    for b in buttons:
        b.config(text=" ", state="normal")
    # → Buttons wieder aktiv machen und leeren

    turn.config(text="Am Zug: X")
    result.config(text="")
    # → Anzeigen zurücksetzen


turn = tk.Label(root, text="Am Zug: X", font=("Arial", 14))
# → zeigt aktuellen Spieler an
turn.pack()

frame = tk.Frame(root)
# → Container für das Spielfeld
frame.pack()

for i in range(9):
    b = tk.Button(
        frame,
        text=" ",
        font=("Arial", 20),
        width=4,
        height=2,
        command=lambda i=i: click(i)
    )
    # → erstellt 9 Buttons (3x3 Feld)

    b.grid(row=i//3, column=i%3)
    # → ordnet Buttons in einem Raster an

    buttons.append(b)
    # → speichert Button für später

result = tk.Label(root, text="")
# → zeigt Ergebnis (Sieg oder Unentschieden)
result.pack()

tk.Button(root, text="Neu starten", command=reset).pack()
# → Reset-Button

root.mainloop()
# → startet die App (Fenster bleibt offen)
