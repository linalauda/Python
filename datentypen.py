# Variablen mit verschiedenen Datentypen
ganzzahl = 42
kommazahl = 3.14
komplexe_zahl = 2 + 3j
wahrheitswert = True
zeichenkette = "Hallo"
liste = [1, 2, 3]
tupel = (1, 2, 3)
menge = {1, 2, 3}
unveraenderliche_menge = frozenset([1, 2, 3])
woerterbuch = {"a": 1, "b": 2}
byte_sequenz = b"abc"
byte_array = bytearray(b"abc")
nichts = None

# Alles in einer Liste für einfache Ausgabe
objekte = [
    ganzzahl, kommazahl, komplexe_zahl, wahrheitswert,
    zeichenkette, liste, tupel, menge, 
    unveraenderliche_menge, woerterbuch,
    byte_sequenz, byte_array, nichts
]

# Ausgabe mit Typ
for obj in objekte:
    print(f"Wert: {obj}, Typ: {type(obj)}")

    ganzzahl = 42
    kommazahl = 3.14
    komplexe_zahl = 2 + 3j
    wahrheitswert = True
    zeichenkette = "Hallo"
    liste = [1, 2, 3]
