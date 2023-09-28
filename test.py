import os
from addOutro import *

# Julian wus here

print("In test.py ...")
for file in os.listdir("."):
    print("file: " + file)
#	if file.startswith("gen") and file.endswith(".mp4") and "Outro" not in file:
#		addOutro(file, "outtro.mp3")