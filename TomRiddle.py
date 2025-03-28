import time
def countdown():
  s = "hi its Tom Riddel. I'm glad you found my code, destroy this curse "
  e = s.split(' ')
  t = len(e)
  while t > 0:
    for i in range(0,t):
      print(e[i])
      t -= 1
      time.sleep(1)

countdown()




