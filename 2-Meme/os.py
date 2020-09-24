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
    os.mkdir(mapnaam)