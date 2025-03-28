"این کد کوچکترین عددی که به n عدد طبیعی متوالی بخش پذیر است را برمیگرداند."
lit =[]
def smallest(n):
  flag = False
  for i in range(50000000,500000000):
    for j in range(1,n+1):
      if i%j == 0:
        flag = True
      else:
        continue
    if flag:
      lit.append(i)

  return lit , flag

def main():
  x = int(input("enter the  number: "))
  s = smallest(x)
  m = min(s)
  print(f'the smallest positive number that is evenly divisible by all of the numbers from 1 to {x}  is :',m  )

main()