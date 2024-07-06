class Game:
  def __init__(self, board_size=5):
    self.board_size = board_size
    self.board = [['_' for _ in range(board_size)] for _ in range(board_size)]
    self.turn = 'x'
    self.game_over = False
  
  def display_board(self):
    """
    Display the current state of the board.
    """
    board = self.board
    print("\n\n")
    print("             |       |       |       |      ")
    print(f"         {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |   {board[0][3]}   |   {board[0][4]}   ")
    print(f"      _______|_______|_______|_______|_______")
    print(f"             |       |       |       |      ")
    print(f"         {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |   {board[1][3]}   |   {board[1][4]}   ")
    print(f"      _______|_______|_______|_______|_______")
    print(f"             |       |       |       |      ")
    print(f"         {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |   {board[2][3]}   |   {board[2][4]}   ")
    print(f"      _______|_______|_______|_______|_______")
    print(f"             |       |       |       |      ")
    print(f"         {board[3][0]}   |   {board[3][1]}   |   {board[3][2]}   |   {board[3][3]}   |   {board[3][4]}   ")
    print(f"      _______|_______|_______|_______|_______")
    print(f"             |       |       |       |      ")
    print(f"         {board[4][0]}   |   {board[4][1]}   |   {board[4][2]}   |   {board[4][3]}   |   {board[4][4]}   ")
    print(f"             |       |       |       |      ")
    print("\n\n")

  def is_winner(self, player):
    """
    Check 4-in-a-row wins of the board
    """
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
    if self.is_winner('x') or self.is_winner('o'):
      return False
    if all(self.board[row][col] != '_' for row in range(self.board_size) for col in range(self.board_size)):
      return True
    return False

  def is_valid_move(self, move):
    """
    Check if the move is valid
    """
    row, col = move
    if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '_':
      return True
    return False

  def make_move(self, move, player):
    """
    Place player's marker on the board and update turn
    """
    if self.turn == player and self.is_valid_move(move):
      row, col = move
      self.board[row][col] = player
      self.turn = 'o' if player == 'x' else 'x' # update turn

  def play(self):
    pass

#game = Game()
#game.display_board()
#game.make_move((0, 0), 'x')
#game.display_board()
#game.make_move((0, 1), 'o')
#game.display_board()