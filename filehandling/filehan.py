
f =  open("doop.txt")
data = f.read()
print(data)
f.close()


# with open("doop.txt") as f:
#   print(f.read(3)) #read(3) -- read only 3 characters 


# with open("doop.txt") as f:
#   print(f.readline(),end="") 
#   print(f.readline()) 
  
  

# with open("doop.txt") as f:
#   for x in f:
#     print(x,end="")



# with open("doop.txt","a") as f:
#   f.write("guntur")


# with open("doop.txt","w") as f:
#   f.write("i have deleted the old data")


# with open("doop1.txt","x") as f:
#   f.write("this is the new file created")
  
# to delete a file we must install os module
import os 
os.remove("doop1.txt")

if os.path.exists("doop1.txt"):
  os.remove("doop1.txt")
  print("file removed successfully")
else:
  print("file doenst exist")  
    

    
   


