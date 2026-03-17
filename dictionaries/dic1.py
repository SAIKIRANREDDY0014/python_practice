dict  = {
  "sai" : 33,
  "ashok" : 99,
  "mall" : "mother",
  "lists" : [1,2,3,5]

}

d2 = {} # empty dictionary

print(dict,type(dict))
print(dict["ashok"])
print(dict["lists"])

print(dict.keys())
print(dict.values())
print(dict.items())
dict.update({"sai":100})
print(dict.items())
dict.update({"praveen":"broinlaw"})
print(dict.items())
print(dict.get("ashok"))  #gives none if val not exists 

print(dict.pop('lists'))
print(dict.items())

print(dict.popitem())
print(dict.items())





