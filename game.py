from algo import minimax
from copy import copy

class Game:
  def __init__(self, board_size=5):
    self.board_size = board_size
    self.board = [['-' for _ in range(board_size)] for _ in range(board_size)]
    self.turn = 'x'
  
  def display_board(self):
    """Display the current state of the board."""
    board = self.board
    n = self.board_size
    print("\n\n")
    print(f"             {"|       " * (n-1)}")
    for row in range(n):
      row_str = f"         {board[row][0]}   |"
      for col in range(1, n):
        row_str += f"   {board[row][col]}   {'|' if col < n-1 else ''}"
      print(row_str)
      if row < n - 1:
        print(f"      {'_______|' * (n-1)}_______")
        print(f"             {"|       "*(n-1)}")
    print(f"             {"|       "*(n-1)}")
    print("\n\n")

  def is_winner(self, player):
    """Check 4-in-a-row wins of the board."""
    n = self.board_size

    # check all rows
    for row in range(n):
      if all(self.board[row][col] == player for col in range(n-1)) or all(self.board[row][col] == player for col in range(1, n)):
        return True
    
    # check all columns
    for col in range(n):
      if all(self.board[row][col] == player for row in range(n-1)) or all(self.board[row][col] == player for row in range(1, n)):
        return True

    # check all diagonals
    if all(self.board[i][i] == player for i in range(n-1)) or all(self.board[i][i] == player for i in range(1, n)):
      return True
    if all(self.board[i][n - i - 1] == player for i in range(n-1)) or all(self.board[i][ n - i - 1] == player for i in range(1, n)):
      return True
    
    return False
  
  def is_draw(self):
    """Check if the game is draw."""
    if any('-' in row for row in self.board):
      return False
    return True

  def is_valid_move(self, move):
    """
    Check if the move is valid.
    """
    row, col = move
    if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '-':
      return True
    return False

  def make_move(self, move, player):
    """Place player's marker on the board."""
    if self.turn == player and self.is_valid_move(move):
      row, col = move
      self.board[row][col] = player
      self.turn = 'o' if player == 'x' else 'x'
      return True
    else:
      return False

def play():
  """Main game loop."""
  game = Game()
  print("Welcome to 5x5 Tic-Tac-Toe!")
  print("Please choose your marker (x/o)")
  player = input()
  while player != 'x' and player != 'o':
    print("Please choose your marker (x/o)")
    player = input()
  ai = 'x' if player == 'o' else 'o'

  while True:
    print(f"Player {game.turn}'s turn.")
    game.display_board()
    if game.turn == ai:
      board = copy(game.board)
      _, move = minimax(board, ai, 100, True)
      game.make_move(move, ai)
    else:
      while True:
        try:
          move_str = input(f"Your turn, please enter your move (row col): ")
          move = tuple(map(int, move_str.split()))
          if game.make_move(move, player):
            print(f"You placed {player} at {move[0], move[1]}")
            break
          else:
            print("Invalid move. Please try again.")
        except ValueError:
          print("Invalid input format. Please enter row and column as integers.")

    if game.is_winner(game.turn):
      print(f"Player {game.turn} won!")
      break
    elif game.is_draw():
      print("Draw!")
      break

  print("Play again? (yes/no)")
  if input() == "yes":
    play()
  else:
    print("Quitting...")
    return

if __name__ == "__main__":
  play()