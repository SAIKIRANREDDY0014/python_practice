with open("doop1.txt","r") as f:
    data = f.read()
    l =["donkey","stupid","idiot"]
    for x in l:
        if(x in data):    
           data = data.replace(x,"#####")
    with open("doop1.txt","w") as f1:
      f1.write(data)