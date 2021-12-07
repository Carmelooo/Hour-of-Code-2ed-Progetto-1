import re
from typing import Pattern

while True:
    
    password=input("Dimmi la password da testare: ")

    valida = True

    # La password deve essere lunga almeno 8 caratteri
    if (len(password)<8): 
        print("\n\nLa password deve avere almeno 8 caratteri\n\n")
        valida=False
        
    
    # La password deve contenere almeno un carattere maiuscolo
    if not (re.search("[A-Z]+",password)):
        print("\n\nLa password deve conterene almeno un carattere maiuscolo\n\n")
        valida=False


    # La password deve contenere almeno un carattere minuscolo
    if not (re.search("[a-z]+",password)):
        print("\n\nLa password deve conterene almeno un carattere minuscolo\n\n")
        valida=False

    
    # La password deve contenere almeno un numero
    if not (re.search("[0-9]+",password)):
        print("\n\nLa password deve conterene almeno un numero\n\n")
        valida=False



    # La password deve contenere almeno un carattere speciale: .,_-
    if not (re.search("[\.,_-]",password)):
        print("\n\nLa password deve contenere almeno uno dei seguenti caratteri speciali: .,_-\n\n")
        valida=False

    if valida:
        print("\n\nLa password è valida!\n\n")
        break
    else:
        continue

    
print("Chiudo il programma.")