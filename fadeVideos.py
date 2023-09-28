import sys
import os 
import numpy as np
import subprocess
import time
from datetime import datetime

count = 0

#for file in os.listdir("withOutro_renamed"):
for file in os.listdir("Staging"):

	if file.endswith(".mp4"):
	
		(file_name,extension) = file.split(".")
#		old_file = ".\withOutro_renamed\\" + file
		old_file = ".\Staging\\" + file
		new_file = ".\withFade\\" + file
		
		print ("\nadd fade-in and fade-out ...")
		print("old_file:",old_file)
		print("new_file:",new_file)
		
		result = subprocess.run(["ffprobe", old_file], capture_output=True)
		
		ffprobe_results = str(result.stderr)
		
		duration_index = ffprobe_results.rfind("Duration")
		duration_start = duration_index + 10
		duration_end   = duration_index + 21
		
		duration = ffprobe_results[duration_start:duration_end]
		
		print("duration:", duration, end="   ")
		
		length  = duration.split(":")
		hours   = int(length[0])
		minutes = int(length[1])
		seconds = length[2].split(".")
		seconds = int(seconds[0])
		
		fade_in_end    = 4
		fade_out_start = (60 * hours) + (60 * minutes) + seconds - 4
		
		print("fade_out_start:", fade_out_start)
		
		# ffmpeg -i gen_intro2.mp4 -vf "fade=t=in:st=0:d=4,fade=t=out:st=nnn:d=4" -c:a copy gen_intro2_fade.mp4
				
		ffmpeg_command = "ffmpeg -i " + old_file + " -vf \"fade=t=in:st=0:d=4,fade=t=out:st=" + str(fade_out_start) + ":d=4\" -c:a copy " + new_file 
		print("ffmpeg_command:",ffmpeg_command)
		
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
		log = open("conversion.log", "a")
		log.write(log_record)
		log.close()

		count += 1
		time.sleep(1)
			
		if count == 11:
		
			exit()