with open("poems.txt") as f:
    if("twinkle" in f.read()):
        print("it is present")
    else:
        print("it doesnt exist") 