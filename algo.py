from math import inf
import random

# helper functions
def check_winner(board):
  size = len(board)
    
  # Check rows
  for i in range(size):
    for j in range(size - 3):
      if (board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]) and (board[i][j] != '_'):
        return board[i][j]
    
  # Check columns
  for i in range(size - 3):
    for j in range(size):
      if (board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]) and (board[i][j] != '_'):
        return board[i][j]
    
  # Check main diagonals
  for i in range(size - 3):
    for j in range(size - 3):
      if (board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]) and (board[i][j] != '_'):
        return board[i][j]
    
  # Check secondary diagonals
  for i in range(3, size):
    for j in range(size - 3):
      if (board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]) and (board[i][j] != '_'):
        return board[i][j]
    
  # Check draw
  for i in range(size):
    for j in range(size):
      if board[i][j] == '-':
        return None

  return "draw"

# evaluation
def evaluate(board, ai, human):
  score_ai = 0
  score_human = 0
  size = len(board)

  # Check rows and columns for sequences of 2 and 3
  for i in range(size):
    for j in range(size - 1):
      row_segment = board[i][j:j+2]
      col_segment = [board[k][i] for k in range(j, j+2)]
      if row_segment.count(ai) == 2 and '-' in row_segment:
        score_ai += 10
      if row_segment.count(human) == 2 and '-' in row_segment:
        score_human += 10
      if row_segment.count(ai) == 3:
        score_ai += 100
      if row_segment.count(human) == 3:
        score_human += 100
      if col_segment.count(ai) == 2 and '-' in col_segment:
        score_ai += 10
      if col_segment.count(human) == 2 and '-' in col_segment:
        score_human += 10
      if col_segment.count(ai) == 3:
        score_ai += 100
      if col_segment.count(human) == 3:
        score_human += 100

  # Check diagonals for sequences of 2 and 3
  for i in range(size - 1):
    for j in range(size - 1):
      diag1_segment = [board[i+k][j+k] for k in range(2)]
      diag2_segment = [board[i+k][j+1-k] for k in range(2)]
      if diag1_segment.count(ai) == 2 and '-' in diag1_segment:
        score_ai += 10
      if diag1_segment.count(human) == 2 and '-' in diag1_segment:
        score_human += 10
      if diag1_segment.count(ai) == 3:
        score_ai += 100
      if diag1_segment.count(human) == 3:
        score_human += 100
      if diag2_segment.count(ai) == 2 and '-' in diag2_segment:
        score_ai += 10 
      if diag2_segment.count(human) == 2 and '-' in diag2_segment:
        score_human += 10
      if diag2_segment.count(ai) == 3:
        score_ai += 100
      if diag2_segment.count(human) == 3:
        score_human += 100
  
  return score_ai - score_human

# adapt the max depth of  to the board
def adaptive_max_depth(board):
  empty = 0
  n = len(board)
  for i in range(n):
    for j in range(n):
      if board[i][j] == '-':
        empty += 1
  if empty >= 20:
    return 3
  elif 12 <= empty < 20:
    return 5
  elif 6 <= empty < 12:
    return 6
  else:
    return 8

#minimax with alpha-beta pruning
def minimax(board, ai, human, depth, is_maximizing, alpha, beta, max_depth=3):
  result = check_winner(board)
  if result:
    if result == 'x':
      return 200 + depth, None
    elif result == 'o':
      return -200 - depth, None
    elif result == "draw":
      return 0, None
  if depth > max_depth:
    return evaluate(board, ai, human), None
  
  if is_maximizing:
    best_move, best_score = None, -inf
    rows = list(range(len(board)))
    random.shuffle(rows)
    cols = list(range(len(board)))
    random.shuffle(rows)
    for i in rows:
      for j in cols:
        if board[i][j] == '-':
          board[i][j] = ai
          score, _= minimax(board, ai, human, depth + 1, False, alpha, beta, adaptive_max_depth(board))
          board[i][j] = '-'
          if score > best_score:
            best_move = (i,j)
            best_score = score
          alpha = max(alpha, best_score)
          if beta <= alpha:
            break
    return best_score, best_move
  else:
    best_move, best_score = None, inf
    rows = list(range(len(board)))
    random.shuffle(rows)
    cols = list(range(len(board)))
    random.shuffle(rows)
    for i in rows:
      for j in cols:
        if board[i][j] == '-':
          board[i][j] = human
          score, _= minimax(board, ai, human, depth + 1, True, alpha, beta, adaptive_max_depth(board))
          board[i][j] = '-'
          if score < best_score:
            best_move = (i,j)
            best_score = score
          beta = min(beta, best_score)
          if beta <= alpha:
            break
    return best_score, best_move

# api for making move using above algorithms
def ai_move(game, ai, human):
  board = game.board
  _, best_move = minimax(board, ai, human, 0, True, -inf, inf)
  return best_move