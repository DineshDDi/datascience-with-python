import random
 
a = 10
b = int (a*random.random()+1)
chances = 3
c = 0
while chances > 0:
  while b != c:
    c = int(input('enter the value: '))
    if c > 0:
      if c > b:
        print("B is smallest number")
        chances -= 1
        if chances == 0:
          print("Your Lose, Sorry you have no more chances")
          break
      elif c < b:
        print("B is biggest number")
        chances -= 1
        if chances == 0:
          print("Your Lose, Sorry you have no more chances")
          break
    else:
      print("Your Lose, Sorry you have no more chances")
      break
  else:
    print("Your winner")
    break