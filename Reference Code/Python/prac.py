# ------------- List -----------------
li = []

#.append() 
for i in range(1,6):
    li.append(i)
print(li)

#.insert()
li.insert(6,6)
print(li)

#.remove(value)
li.remove(6)
print(li)

#.pop(index)
li.pop(4)
print(li)

#list[x:y x included y not]
print(li[1:3])

#traversing
for i in range(0,len(li)):
    print(li[i])


# ---------------- String Manupilation ------------------------
str = "Hello My name is Kavy Solanki"
str2 = "      ----No one----        "

#.split(Default - space, Can Specify keyword)
print(str.split("a"))
    #print(str.split())

#.join() - used to joina set
str1 = " ".join(["Hello", "My", "name", "Kavy"])
print(str1)

#.replace("old one", "replace with", "how many")
print(str1.replace("a", "A"))
    #print(str1.replace("a", "A", 1))

#.split(),lstrip(),rstrip() to from left and right only resp
print(str2)
print(str2.strip())
print(str2.strip().strip("-"))

#.lower() and .upper()
print(str.lower())
print(str.upper())


# ---------------- Dictionaries ----------------
random = {"A": "Apple", "B": "Ball", "C" : "Cat", "D" : "Dog"}

#.get(key)
print(random.get("A"))

#.keys()
print(random.keys())

#.values()
print(random.values())

#.items()
print(random.items())

#.update()
random.update({"A": "Amanda"})
#random.update(A='Apple')
print(random)

#.pop()
random.pop("A")
print(random)
