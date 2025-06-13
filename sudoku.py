import json
import time
import os

PUZZLE = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

SOLUTION = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += (str(val) if val != 0 else ".") + " "
        print(row_str)


def board_full(board):
    return all(all(cell != 0 for cell in row) for row in board)


def load_scores():
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_scores(scores):
    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=2)


def main():
    scores = load_scores()
    name = input("Enter your name: ")

    board = [row[:] for row in PUZZLE]
    print("Sudoku puzzle:")
    print_board(board)
    start = time.time()

    while not board_full(board):
        entry = input("Enter row col value (e.g. '1 3 9') or 'q' to quit: ")
        if entry.lower() == 'q':
            print('Quitting...')
            return
        try:
            r, c, v = map(int, entry.split())
            if PUZZLE[r-1][c-1] != 0:
                print("Cell is fixed. Choose another.")
                continue
            if not 1 <= v <= 9:
                print("Value must be between 1 and 9.")
                continue
            board[r-1][c-1] = v
        except Exception:
            print("Invalid input. Use format 'row col value'.")
            continue
        print_board(board)

    end = time.time()
    elapsed = int(end - start)

    if board == SOLUTION:
        print("Congratulations, you solved the puzzle!")
        score = max(0, 1000 - elapsed)
        print(f"Time taken: {elapsed} seconds. Score: {score}")
        scores[name] = scores.get(name, 0) + score
        save_scores(scores)
        print("\nScoreboard:")
        for n, s in scores.items():
            print(f"{n}: {s}")
    else:
        print("Incorrect solution. Try again next time.")


if __name__ == "__main__":
    main()
