age_var = 28
my_str = "My name is {name} and I'm {age} years old.".format(name="Joe", age=age_var)
print(my_str)

#String replication
greeting = "Hallo!"
print(greeting * 3)

#Sub string part 1
my_string = "Hello World"
print(my_string[1])  #e
print(my_string[-1]) #d
print(my_string[0:5]) #Hello
print(my_string[6:])  #World
print(my_string[:5])  #Hello
print(my_string[::2]) #HloWrd
print(my_string[::-1]) #dlroW olleH
print(my_string[1:5:2]) #el
print(my_string[::1]) #dlroW olleH
print(my_string[:1]) #dlroW olleH