
import string
def a1(str1, str2):

    wynik = set()
    for letter in str1:
        if letter in str2 and letter.isalpha():
            wynik.add(letter)
    for letter in str2:
        if letter in str1 and letter.isalpha():
            wynik.add(letter)
    
    return wynik

def a2(str1, str2):
  wynik = set()
  for letter in str1:
    if letter.isalpha():
      wynik.add(letter)
  for letter in str2:
    if letter.isalpha():
      wynik.add(letter)
    
  return wynik


def a3(str1, str2):
  wynik = set()
  litery = string.ascii_letters +"ĄĆŚŻŹŃŁÓąćśżźńłó"
  for letter in litery:
    if letter not in str1 and letter not in str2:
      wynik.add(letter)
    
  return wynik

def a4(str1, str2):
  wynik = set()
  for letter in str1:
    if letter in str2 and not letter.isalpha():
      wynik.add(letter)
  for letter in str2:
    if letter in str1 and not letter.isalpha():
      wynik.add(letter)
    
  return wynik

def a5(str1, str2):
  wynik = set()
  for letter in str1:
    if not letter.isalpha():
      wynik.add(letter)
  for letter in str2:
    if not letter.isalpha():
      wynik.add(letter)
    
  return wynik



def main():
    str1m = "Kobyła ma,"
    str2m = "mały bok"
    print(str1m)
    print(str2m)
    print(a1(str1m,str2m))
    print(a2(str1m,str2m))
    print(a3(str1m,str2m))
    print(a4(str1m,str2m))
    print(a5(str1m,str2m))    
    return



if __name__ == "__main__":
  main()