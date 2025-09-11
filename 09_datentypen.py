#1 Ganzzahl (int)
age: int = 25
print (age) # Ausgabe: 25

# 2 Fleißkommazahl (float)
pi: float = 3.14159
print(pi) # Ausgabe: 3.14159

# 3 Wahrheitswerte (bool)
is_active: bool = True
print(is_active)  # Ausgabe: True

# 4 Zeichenketten (str)
name: str = "Alina"
print(name)  # Ausgabe: Alina

# 5 Listen (list) – veränderbar
fruits: list[str] = ["Apfel", "Banane", "Kirsche"]
fruits.append("Orange")
print(fruits)  # Ausgabe: ['Apfel', 'Banane', 'Kirsche', 'Orange']

# 6 Tupel (tuple) unveränderbar
coordinates: tuple[float, float] = (52.5, 13.4)
print(coordinates) #Ausgabe: (52.5, 13.4)

# 7 Mengen(set) - keine Dublikate Reihenfolge ist egal 
unique_numbers: set[int] = {1,2,3,3,2}
print(unique_numbers ) # Ausgabe {1,2,3}


# 8️⃣ Dictionaries (dict) – Schlüssel/Wert-Paare
person: dict[str, str , int] = {
    "name": "Eva",
    "age": 7
}
print(person["name"])  # Ausgabe: Eva

# 9️⃣ NoneType – spezielle "kein Wert"-Variable
result: None = None
print(result)  # Ausgabe: None