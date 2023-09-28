import sys
import os 
import numpy as np

count = 0
print ("renaming .mp4 files in")
for file in os.listdir("withOutro"):

	if file.endswith(".mp4"):
	
			renamedFile = file.replace("_withOutro", "")
			
			old_file = os.path.join(".\withOutro", file)
			new_file = os.path.join(".\withOutro_renamed", renamedFile)
	
			print ("old_file:", old_file)
			print ("new file:", new_file)
			
			os.rename(old_file, new_file)
