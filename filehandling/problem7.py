with open("log.txt","r") as f:
   count = 0
   data =  f.readlines()
  
for line in data:
    count = count+1
    if("python" in line):
        print(f"it contains in line number : {count}")
        break 
else:
    print("it doesnt contain")   