# The goal of this program is to practice Python constructs

def sumDigits(x):
   sum = 0
   while x>0:
     sum+=x%10
     x//=10
   return sum

def getNumber():
   symbols = input("Enter a digit: ")
   combine = ""
   symbols = int (symbols)
   while symbols >=0:
     combine += str (symbols)
     symbols = input("Enter a digit: ")
     symbols = int (symbols)
   return combine

def sumTwo(a,b):
   c = a + b
   return c

print (sumDigits(6969))

print (getNumber())

x = sumTwo(3,5)
print(x)


