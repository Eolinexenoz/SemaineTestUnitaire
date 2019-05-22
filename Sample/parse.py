def recupereinput():
    enteredstring = input()
    parsebeginningenteredstring(enteredstring)

def parsebeginningenteredstring(enteredstring):
    if enteredstring[1].isalpha():
        print("Mauvaise entree, veuillez saisir un chiffre en premier")

