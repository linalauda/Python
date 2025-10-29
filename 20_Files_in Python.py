# Öffnen oder erstellen der Datei zum Schreiben ("w" = write)
with open("python123.txt", "w") as file:
    file.write("Hallo, das ist meine erste Datei mit Python!\n")
    file.write("Ich lerne gerade, wie man Dateien liest und schreibt.\n")

print("Datei erfolgreich erstellt und Text gespeichert!")


with open("python123.txt", "r") as file:
    content = file.read()  # Lies den ganzen Inhalt
    print("Dateiinhalt:")
    print(content)

# Anhängen von Text an die bestehende Datei ("a" = append)
with open("python123.txt", "a") as file:
    file.write("Das ist eine zusätzliche Zeile, die angehängt wurde.\n")   

print("Text erfolgreich angehängt!")

with open("python123.txt", "r") as file:
    for line in file:
        print("Zeile:", line.strip())

import os

# Überprüfen, ob die Datei existiert
#if os.path.exists("python123.txt"):
#   os.remove("python123.txt")
#    print("Datei 'python123.txt' wurde gelöscht.")
#else:   
#    print("Die Datei 'python123.txt' existiert nicht.") 


if os.path.exists("python123.txt"):
    print("Datei existiert!")
else:
    print("Datei nicht gefunden.")
