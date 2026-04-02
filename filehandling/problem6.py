with open("log.txt","r") as f:
   
   data =  f.read()
   if("python" in data):
      print("it contains")
   else:
       print("it doesnt contains")