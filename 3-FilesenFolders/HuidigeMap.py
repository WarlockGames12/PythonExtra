# hier importeer je de os module
import os
mapnaam = 1
# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

running = True

while running: 
    # De letters cwd staan voor: Current working directory (de huidige map!)
    # Een nieuwe map maken met os.mkdir()
    mapnaam += 1
    os.mkdir(str(mapnaam))
    if mapnaam == 10:
        print("Het is nu vol")
        running = False
         
    else: 
        print("let's fill it up")




mapnaam = 1
running = True


while running:
     # De letters cwd staan voor: Current working directory (de huidige map!)
     # Een nieuwe map maken met os.mkdir()
     mapnaam += 1
     os.rmdir(str(mapnaam))
     if mapnaam == 10:
        print("Het is nu leeg")
        running = False
         
     else: 
        print("Let's Delete it :D")