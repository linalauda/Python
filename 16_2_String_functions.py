text = "Hallo {1}, wilkommen in {0}, heute ist {2}.".format("Lina", "Python", "3.11")
print(text)

#substring part 1
my_string = "Hello World"
print(my_string[0])  #H
print(my_string[-2]) #d

#substring part 2
print(my_string[0:5]) #Hell
print(my_string[6:])  #World
print(my_string[:5])  #Hello

#substring part 3
print(my_string[::2]) #HloWrd
#print(my_string[::-1]) #dlroW olleH
#print(my_string[1:5:2]) #el
#print(my_string[::1]) #Hello World
#print(my_string[:1]) #H

print(my_string[::1])
print(my_string[::-1])
print(my_string[::2])
print(my_string[::-2])
print(my_string[::3])
print(my_string[::-3])

print(my_string[0::])
print(my_string[1::])
print(my_string[0::4])

#join function
my_list = ['H', 'e', 'l', 'l', 'o']
print(''.join(my_list))
print(' '.join(my_list))
print(', '.join(my_list))
print('---'.join(my_list)) 

#join
teile = ["Hallo", "Welt", "wie", "geht's?"]
text = " ".join(teile) #Leerzeichen als Trennzeichen
print(text)

#split function
text = "Apfel Birne Kirsche"
liste = text.split()
print(liste)

text2 = "eins,zwei,drei,vier"
liste2 = text2.split(",") #Komma als Trennzeichen
print(liste2)   
#split
text = "Hallo Welt wie geht's?"
liste = text.split(".") #Leerzeichen als Trennzeichen
print(liste)

#replace function
text = "Hallo Welt"
new_text = text.replace("Welt", "Python")
print(new_text)

#replace
text1 = "ich liebe Java, Java ist toll!"
new_text1 = text1.replace("Java", "Python")
print(new_text1)

#lower and upper function
text = "Hallo Welt"
print(text.lower())
print(text.upper())     