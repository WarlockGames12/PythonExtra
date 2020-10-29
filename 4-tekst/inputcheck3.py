import re

while True:

    invoer = input("Voer je kenmerk in in: ")

    # Het klopt dat er een "r" voor de regular expression staat, zo voorkom je gedoe met speciale tekens
    patroon = r"[A-Z]{2}-[0-9]{3}-[A-Z]{3}"
    matches = re.findall(patroon, invoer)
    
    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het kenmerk in het juiste formaat ingevoerd is.
print("Bedankt kenmerk in juiste formaat:", matches[0])
