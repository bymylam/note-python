#basic code
print("Hello World")

#drawing a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#VARIABLES & DATA TYPES
character_name = "Tom" #quotation marks only for string
character_age = "50"
character_number = 50.5678213
is_male = False
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
character_name = "Mike" #updating the variable
print("he really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

#WORKING WITH STRINGS
print("Giraffe\nAcademy") #insert a new line
print("Girraffe\"Academy") #print out a quotation mark
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper()) #boolean: see if a string is entirely uppercase
print(phrase.upper().isupper()) #combination. convert it into uppercase, then (boolean)
print(len(phrase))
print(phrase[0]) #G is index 0
print(phrase[3]) #usually in index function
print(phrase.index("G")) #find the index
print(phrase.index("Academy"))
#print(phrase.index("z")) #ERROR
print(phrase.replace("Giraffe", "Elephant"))