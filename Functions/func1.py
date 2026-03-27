def printnam(name):
  print("Sai kiran reddy: ",name)

def addnum(a,b):
  return a+b

def defpara(name,lastname="reddy"):
  print(name+lastname)
      
# printnam("ashokreddy")  
# a = addnum(55,6)
# print(a)

# defpara("sai")
# defpara("sai","kiran")


# # factorial using recursion

# fact =0;
# def factorial(n):
#   if(n == 0 or n == 1):
#     return 1
#   fact = factorial(n-1) * n
#   return fact  

# f= factorial(5)
# print(f)


# print("sai")
# print("kiran", end ="")
# print("reddy",end="")
# print("emani")

# sum of n natural numbers
def sumofn(n):
  if(n == 1):
    return 1
  sum = n + sumofn(n-1)
  return sum;

print(sumofn(6))
  
