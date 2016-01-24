n = int(input("Start value"))

def fizzbuzz(i):
 if (i%2 == 0 and i%3 == 0):
   return "fizzbuzz"
 if (i%2 == 0):
   return "fizz"
 if (i%3 == 0):
   return "buzz"
 if (i%3 != 0 and i%2 != 0):
   return str(i)
 


for i in map(fizzbuzz,range(1,n)):
 print(i) 
