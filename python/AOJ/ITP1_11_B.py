class Dice:
  arr = []
  def __init__(self, arr):
    self.arr = arr
  def move(self, pos):
    if pos == 'E':
      self.eastMove()
    elif pos == 'N':
      self.northMove()
    elif pos == 'S':
      self.sorthMove()
    elif pos == 'W':
      self.westMove()
  def out(self):
    return self.arr[0]
  def eastMove(self):
    [self.changeArr(3, n) for n in [6,4,1]]
  def northMove(self):
    [self.changeArr(5, n) for n in [6,2,1]]
  def sorthMove(self):
    [self.changeArr(2, n) for n in [6,5,1]]
  def westMove(self):
    [self.changeArr(4, n) for n in [6,3,1]]
  def changeArr(self, f, t):
    tmp = self.arr[f - 1]
    self.arr[f - 1] = self.arr[t - 1]
    self.arr[t - 1] = tmp
diceNum = list(map(int, input().split(' ')))
dice = Dice(diceNum)
l = input()
for a in l:
  dice.move(a)
print(dice.out())