import re

emails = []

with open("tekstmetmails.txt", "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)
        
        # Alle gevonden emails aan de email list toevoegen
        emails.extend(gevonden)
        
        # Volgende regel lezen
        regel = bestand.readline()

print(emails)



