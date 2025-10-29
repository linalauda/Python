# 18_Collections.py
# Listen, Tupel, Sets und Dictionaries
fruits = ["Apfel", "Banane", "Kirsche"]
print(fruits)

#Tupel
coordinates = (10, 20)
print(coordinates)

#Sets
colors = {"rot", "blau", "grün"}
print(colors)

#Dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

empty_set = ("aaa", "bbb")  
print(empty_set)       # ➜ set()
print(type(empty_set)) # ➜ <class 'set'>

string_set = {"Apfel", "Banane", "Kirsche"}
print(string_set)   # ➜ {'Apfel', 'Banane', 'Kirsche'}
print(type(string_set)) # ➜ <class 'set'>

number_set = {1, 2, 3, 4, 5}
print(number_set)   # ➜ {1, 2, 3, 4, 5}
print(type(number_set)) # ➜ <class 'set'>

mixed_set = {1, "Apfel", 3.14, True}
print(mixed_set)    # ➜ {1, 3.14, 'Apfel'}
print(type(mixed_set))  # ➜ <class 'set'>


#Set Methoden 

#.add()
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # ➜ {1, 2, 3, 4}

#.remove()
my_set.remove(2)
print(my_set)  # ➜ {1, 3, 4}

#.clear()
my_set.clear()
print(my_set)  # ➜ set()   