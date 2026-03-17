# here we are learning 

s = {1,2,3,4}
print(s)
print(type(s))

s0 = set()
print(type(s))

s1 ={1,1,1,4,4,3,6,7,7}
print(s1)
print(type(s1))

s1.add(5)
print(s1)

s0.add(5)
print(s0)

s0.clear()
print(s0)


print(s)
s.pop() #c removes the first elemet
print(s)

s.remove(4)
print(s)

print(len(s))

s3 = {1,3,4,5}

print(s.union(s3))
print(s.intersection(s3))



