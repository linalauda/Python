früchte = ["Apfel", "Banane", "Kirsche"]
print(früchte[0])  # Apfel

früchte.append("Orange") #fuegt Orange hinzu
print(früchte)

früchte.remove("Banane") #löscht die Banane aus der Liste 
print(früchte)

print(len(früchte)) # zeigt die Zahl der Elementen in der Liste

#"Apfel", "Banane", "Kirsche", "Orange"
#"Apfel", "Kirsche", "Orange"

früchte.pop(1) # Entferne Element an Position 1 (Index 1 = "Kirsche")
#"Apfel", "Kirsche", "Orange"
print(früchte)
#"Apfel", "Orange"

del früchte[1] # Entferne Element an Index 1 (="Orange")
print(früchte)

früchte.append("Orange", "Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere")
print(früchte)

print(len(früchte))

element = früchte.pop(0)
print("Element:" , element)