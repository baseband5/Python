import math

def inputData():
  n = int(input("Ilość danych: "))
  return n

def solve(n):
  sum = 0
  for x in range(0,n):
    prompt = "Podaj liczbę nr "+ str(x+1) + ": "
    a = float(input(prompt))
    sum += ((-1)**(x+1))*(math.factorial(a)/math.factorial(x+1))
  return sum

def main():
  n = inputData()
  print(str(round(solve(n))))

if __name__ == "__main__":
  main()