
import sys as sys
import os

line = '-' * 30
v_bar = '|'

X_total = 7
Y_total = 6

data = [([' ' * 3] * Y_total).copy() for i in range(X_total)]

currentPlayer = 1

def clear(): os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def write(s = ''): sys.stdout.write(str(s))
def writef(s = ''): write(str(s) + '\n')

def render():
  clear()
  for y in range(0, Y_total): 
    writef(line)
    for x in range(0, X_total):
      write(v_bar)
      write(data[x][y])
    writef(v_bar)
  
  writef(line)
  write(' ' * 2)
  for i in range(X_total):
    write(i)
    write(' ' * 3)  

  playerInput()

def checkSlot(x,y):
  slot = data[x][y]
  if slot == 'X':
    return 1
  elif slot == 'O':
    return 2


def checkNearBySlots(x,y, matched= 0):
  result = checkSlot(x, y)
  if result:
    if result == currentPlayer: 
      matched += 1
      if matched == 4: return True
    YPossible = [x, y + 1]
    XPossible = [x + 1, y]
    RPossible = [x + 1, y + 1]
    if (
      checkNearBySlots(x, y + 1, matched) or \
      checkNearBySlots(x + 1, y, matched) or \
      checkNearBySlots(x + 1, y + 1, matched)
    ): return True
  else: return False

def checkForWin():
  if checkNearBySlots(0,0): 
    writef()
    writef('Player ' + str(currentPlayer) + 'WIN!')
    sys.exit()



def playerInput():
  writef()
  try:
    global currentPlayer
    x = int(input('Player ' + str(currentPlayer) + ' please enter a number:'))
    if x > 6 or x < 0: raise Exception()
    for y in range(Y_total - 1, 0 - 1, -1):
      if data[x][y] == ' ' * 3: 
        if currentPlayer == 1: data[x][y] = ' X '
        else: data[x][y] = ' O '
        checkForWin()
        currentPlayer += 1
        if currentPlayer > 2: currentPlayer = 1
        break
  finally: 
    render()
    # playerInput()

def main():
  render()
  


main()