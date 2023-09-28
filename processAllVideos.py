import os
from addOutro import *
for file in os.listdir("."):
	if file.startswith("gen") and file.endswith(".mp4") and "Outro" not in file:
		addOutro(file, "outtro.mp3")