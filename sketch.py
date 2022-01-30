
def main():
    n = int(input("N: "))
    div=getDivisors(n)
    print("Dzielniki:")
    for i in div:
        print(i)
    if( isPerfect(n,div)):
        print("Liczba jest doskonała")
    else:
        print("Liczba nie jest doskonała")

    return

def getDivisors(x):
    divisors = []
    for i in range(1,x//2+1):
        if(x%i==0):
            divisors.append(i)
    return divisors

def isPerfect(num, divisors):
    sumOfDivisors = sum(divisors)
    if (sumOfDivisors == num):
        return True
    else: 
        return False

main()