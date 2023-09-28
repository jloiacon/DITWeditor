import os
import sys
from addOutro import addOutro

file = sys.argv[1]

print ("Overdubbing outro onto" + file)
addOutro(file, "outtro.mp3")