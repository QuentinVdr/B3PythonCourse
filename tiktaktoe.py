def print_board(board):
    print("\n".join(map(str, board)))


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False


def game():
    board = [[' '] * 3 for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"{current_player}'s turn")
        row = int(input("Enter the row - [1, 2, 3]: ")) - 1
        col = int(input("Enter the column | [1, 2, 3]: ")) - 1

        if board[row][col] != ' ' or row > 3 or row < 1 or col > 3 or col < 1:
            print("\nInvalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"\nCongratulations! {current_player} has won the game!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    game()
