board = ["-" , "-" , "-" 
         "-" , "-" , "-" 
         "-" , "-" , "-"]
currentPlayer = "X"
winner = None
gamerunning = True
def  printBoard(board):
     print(board[0] + "|" + board[1] + "|" + board[3])
     print(board[4] + "|" + board[5] + "|" + board[6])
     print(board[7] + "|" + board[8] + "|" + board[9])
printBoard(board)



def playerInput(board):
  inp = int (input ("Enter a number 1-9: "))