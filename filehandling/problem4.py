with open("doop1.txt","r") as f:
    data = f.read()
    newda = data.replace("donkey","#####")
    print(newda)
    with open("doop1.txt","w") as f1:
      f1.write(newda)