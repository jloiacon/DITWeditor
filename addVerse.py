import sys
import os 
import numpy as np
import subprocess
import time
from datetime import datetime

count = 0
Book = "Genesis"

for file in os.listdir("Staging"):

	if file.endswith(".mp4"):
	
		(file_name,extension) = file.split(".")
		old_file = ".\Staging\\" + file
		new_file = ".\withVerse\\" + file
		
		(filename,ext) = file.split('.')
		
		if filename.find('_') >= 0:
			(half1,vend) = filename.split('_')
		else:
			print("Offending file:",filename)

		if filename.find('+') < 0:
			scripture = Book +" "+ vend.title()
			# print("Scripture:", scripture)
			# # continue
		
		# book = half1[0:3]

		# vstart = half1[3:99]
		# (s_chapter,s_verse) = vstart.split('+')
		# (e_chapter,e_verse) = vend.split('+')
		
		# if (s_chapter == e_chapter):
			# scripture = Book +" "+ s_chapter +":"+ s_verse +"-"+ e_verse
		# else:
			# scripture = Book +" "+ s_chapter +":"+ s_verse +"-"+ e_chapter +":"+ e_verse
		
		print("Scripture:", scripture)
		
		if scripture.find(':') >= 0:
			scripture_out = scripture.replace(':','\:')
		else:
			scripture_out = scripture
		
#		ffmpeg -i .\withFade\gen9+6_9+15.mp4 -vf "drawtext=text='Genesis 9\:6-15' :font='Calibri' :fontcolor=white :fontsize=30 x:60 y:30" -codec:a copy .\withVerse\gen9+6_9+15.mp4

		ffmpeg_command = "ffmpeg -i " + old_file + " -vf \"drawtext=text=\'" + scripture_out + "\' :font=\'Calibri\' :fontcolor=white :fontsize=30 :x=60 :y=30\" -c:a copy " + new_file

		print(ffmpeg_command)
		
		current_time = datetime.now()
		start_time = current_time.strftime("%H:%M:%S")
		start_epoch = int(time.time())
		
		result = subprocess.run(ffmpeg_command)
		
		end_epoch   = int(time.time())
		conversion_time = end_epoch - start_epoch
		minutes = int(conversion_time / 60)
		minute_remainder = (conversion_time / 60) - minutes
		seconds = int(minute_remainder * 60)
		conversion_ms = str(minutes) + ":" + str(seconds)
		
		log_record = "Conversion of " + file + " started: " + start_time + " and took: " + conversion_ms + " (min:sec).\n"
		log = open("addverse.log", "a")
		log.write(log_record)
		log.close()

#		count += 1
#		time.sleep(1)
			
		# if count == 15:
		
			# exit()