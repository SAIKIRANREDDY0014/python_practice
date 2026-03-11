print("learning tuples")
a = (1,2,1,4,5,"sai",66.6,True)
b=(3,)
print(type(a))
print(a)
print(b)

print(a[1])
# a[1] = 44
print(a)


print(a.count(1))
print(a.index("sai"))


# operations in tuples
t1 = (1,2,5,6)
t2= ( 3,32,657,3)

concat = t1+t2
print(concat)

print(t1 * 4)
print(3 in t2)

print(len(t1))
print(min(t1))
print(max(t1))

# slicing
print(t1[2:4])

# unpacking
a,b,c,d = t1
print(a,b,c,d)





