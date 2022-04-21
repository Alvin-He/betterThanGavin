
import sys as sys
import os

line = '-' * 30
v_bar = '|'

X_total = 7
Y_total = 6

def clear(): os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def genDataStructure(): return [([' ' * 3] * Y_total).copy() for i in range(X_total)]
def write(s = ''): sys.stdout.write(str(s))
def writef(s = ''): write(str(s) + '\n')

data = genDataStructure()
currentPlayer = 1

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

def checkSlot(x,y):
  if x < 0 or y < 0 or x >= X_total or y >= Y_total: return 0 
  slot = data[x][y]
  if slot == ' X ':
    return 1
  elif slot == ' O ':
    return 2
  else: return 0


def checkNearBySlots(xStart, yStart, xIncerment, yIncerment, _matches = 1):
  xStart += xIncerment
  yStart += yIncerment
  if checkSlot(xStart, yStart) == currentPlayer:
    _matches += 1
    if _matches == 4: return True
    else: return checkNearBySlots(xStart, yStart, xIncerment, yIncerment, _matches)
  else: 
    return False
  
  

def checkForWin(x ,y):
  if(checkNearBySlots(x, y, 1, 0) # positive x direction
  or checkNearBySlots(x, y,-1, 0) # negative x direction

  or checkNearBySlots(x, y, 0, 1) # positive y direction
  or checkNearBySlots(x, y, 0,-1) # negative y direction

  or checkNearBySlots(x, y, 1, 1) # upper y = x direction 
  or checkNearBySlots(x, y,-1,-1) # lower y = x direction

  or checkNearBySlots(x, y,-1, 1) # upper y = -x direction
  or checkNearBySlots(x, y, 1,-1) # lower y = -x direction
  ): return True
  else: return False
  



def gameLoop():
  writef()
  global currentPlayer, data
  try: 
    x = int(input('Player ' + str(currentPlayer) + ' please enter a number:'))
  except:
    pass
  else: 
    if not (x > 6 or x < 0):
      for y in range(Y_total - 1, 0 - 1, -1):
        if data[x][y] == ' ' * 3: 
          if currentPlayer == 1: data[x][y] = ' X '
          else: data[x][y] = ' O '
          if checkForWin(x, y): 
            render()
            writef('player: ' + str(currentPlayer) + ' win')
            try:
              ui = input('Press Something to continue playing or CTRL + C to exit.')
            except KeyboardInterrupt: 
              sys.exit()
            data = genDataStructure()
            currentPlayer = 1
            break
          currentPlayer += 1
          if currentPlayer > 2: currentPlayer = 1
          break
  finally:
    render()
    gameLoop()

def main():
  render() # render the board first
  gameLoop() # then start the game loop

main()