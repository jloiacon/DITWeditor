import sys
import os 
import librosa
import soundfile as sf
import numpy as np
import platform

def addOutro(inVideoFilename, inOutroFilename):
	print("generating filenames")
	inVideoAudioFilename  = inVideoFilename+".mp3"
	combinedAudioFilename = inVideoFilename+"_combined.flac"
	outVideoFilename  = inVideoFilename+"_withOutro.mp4"

	# Check the operating system
	if platform.system() == "Windows":
		ffmpeg_string = "ffmpeg.exe"
	else:
		ffmpeg_string = "ffmpeg"

	print("checking if audio is already extracted")
	#if not os.path.exists(inVideoAudioFilename):
	print("extracting audio from video")
	command = f'{ffmpeg_string} -y -i {inVideoFilename} {inVideoAudioFilename}'
	print("running: " + command)
	os.system(command)
	
	print("loading inputs")
	videoAudio, videoAudioSampleRate = librosa.load(inVideoAudioFilename, sr=None) # sr=None: no sr conversion
	print(videoAudioSampleRate)
	outroAudio, sr = librosa.load(inOutroFilename, sr=videoAudioSampleRate)

	print("add the outro to video audio")
	# python note: the Nth element from the end of an array can be accessed as -N
	videoAudio[-len(outroAudio):] += outroAudio
	# normalize
	videoAudio = videoAudio/max(videoAudio)
	print(np.shape(videoAudio))

	print("writing superimposed audio file")
	# Write out audio as 24bit Flac
	sf.write(combinedAudioFilename, videoAudio, videoAudioSampleRate, format='flac', subtype='PCM_24')

	print("combining with video")
	command =f'ffmpeg -y -i {inVideoFilename} -i {combinedAudioFilename} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {outVideoFilename}'
	print("running: " + command)
	os.system(command)

# Tests specific to this file
if __name__ == "__main__":
	print ("in main ...	")
	addOutro(sys.argv[1], sys.argv[2])