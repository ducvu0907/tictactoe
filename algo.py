from math import inf

# helper functions
def check_winner(board):
  for player in ['x', 'o']:
    n = len(board)
    for row in range(n):
      if all(board[row][col] == player for col in range(n-1)) or all(board[row][col] == player for col in range(1, n)):
        return player
    # check all columns
    for col in range(n):
      if all(board[row][col] == player for row in range(n-1)) or all(board[row][col] == player for row in range(1, n)):
        return player
    # check all diagonals
    if all(board[i][i] == player for i in range(n-1)) or all(board[i][i] == player for i in range(1, n)):
      return player
    if all(board[i][n - i - 1] == player for i in range(n-1)) or all(board[i][n - i - 1] == player for i in range(1, n)):
      return player
  return "draw" if not any('-' in row for row in board) else ""

def get_open_moves(board):
  moves = []
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == '-':
        moves.append((i,j))
  return moves

# minimax without pruning
def minimax(board, player, depth, maximizing):
  winner = check_winner(board)
  if winner == player:
    return (10 + depth, None) if maximizing else (-10 - depth, None)
  elif winner == "draw":
    return 0, None
  elif winner != "":
    return (10 + depth, None) if not maximizing else (-10 - depth, None)
  elif depth == 0:
    return 0, None

  best_move, value = None, None
  opponent = 'x' if player == 'o' else 'o'

  if maximizing:
    for move in get_open_moves(board):
      row, col = move
      board[row][col] = player
      val, _ = minimax(board, opponent, depth - 1, False)
      board[row][col] = '-'
      if not value or val > value:
        best_move = move
        value = val
  else:
    for move in get_open_moves(board):
      row, col = move
      board[row][col] = player
      val, _ = minimax(board, opponent, depth - 1, True)
      board[row][col] = '-'
      if not value or val < value:
        best_move = move
        value = val

  return val, best_move

# minimax with alpha-beta pruning
def minimax_ab(board, player, depth, alpha, beta):
  pass

# api for making move using above algorithms
def move(board):
  pass