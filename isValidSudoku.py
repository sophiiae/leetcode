from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
  dict = {}
  # check if there's no repeated number in array
  def noRepeat(arr):
    dict.clear()
    for x in arr:
      if x == '.':
        continue
      if x in dict:
        return False
      dict[x] = 1
    return True
  
  # check rows
  for row in board:
    if not noRepeat(row):
      return False
  
  # check columns
  for i in range(len(board[0])):
    col = [row[i] for row in board]
    if not noRepeat(col):
      return False
      
  # check boxes
  indexes = [[0,1,2], [3,4,5], [6,7,8]]
  for row in indexes:
    for col in indexes:
      box = []
      for r in row:
        box = box +[board[r][c] for c in col]
      if not noRepeat(box):
        return False
  return True

test1 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

test2 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print('test 1:', 'pass' if isValidSudoku(test1) is False else 'fail')
print('test 2:', 'pass' if isValidSudoku(test2) is True else 'fail')