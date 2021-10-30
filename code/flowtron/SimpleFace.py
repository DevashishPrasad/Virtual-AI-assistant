
import cv2
import scipy.io.wavfile
import numpy as np
import time
import os

img = cv2.imread("face-without-mouth.jpg")

def audio2mouth(audio_rate, audio_data, frame_rate = 30, audio_file = "my_audio.mp4", video_file = "my_video.mp4", op_file="output.mp4"):
  
  audio_data = np.array(audio_data)
  actual_audio_data = audio_data.copy()
  audio_data *= 100000
  
  height, width, channels = img.shape

  # Prepare video writer
  writer = cv2.VideoWriter(filename = video_file,		  				#Provide a file to write the video to
          fourcc=cv2.VideoWriter_fourcc(*"XVID"),            		#Use whichever codec works for you...
          fps=frame_rate,                                        			#How many frames do you want to display per second in your video?
          frameSize=(width, height))                     				#The size of the frames you are writing

  # Preprocess audio array
  aidx = 0
  audio = []
  const_rate = audio_rate//(frame_rate//2)

  while aidx < len(audio_data):
    audio.append(np.mean(audio_data[aidx:aidx+(const_rate)]))
    aidx += const_rate

  audio = np.array(audio)
  audio = audio/2
  audio = np.clip(audio, -40, 40)

  # Write frames into video writer
  half_height = height//2 
  half_width = width//2

  last = None
  for idx,i in enumerate(audio):
    i = int(abs(i))
    if last is None:
      last = i

    # calculate middle
    j = (i+last)//2

    # write previous frame
    new_img = img.copy()
    cv2.ellipse(new_img, (half_height,half_width+60), (60, 10+j), 0, 0, 360, (0,0,0), -1) 
    writer.write(new_img)

    # write current frame
    new_img = img.copy()
    cv2.ellipse(new_img, (half_height,half_width+60), (60, 10+i), 0, 0, 360, (0,0,0), -1) 
    writer.write(new_img)

    last = i
		
  writer.release()

  # Save final output to the disk
  os.system("rm " + audio_file)
  scipy.io.wavfile.write(audio_file, audio_rate, actual_audio_data)
  os.system("rm " + op_file)
  os.system("ffmpeg -i " + video_file + " -i " + audio_file + " -map 0:v -map 1:a -c:v copy -shortest " + op_file)

if __name__ == "__main__":
  	audio_rate, audio_data = scipy.io.wavfile.read("Chianti.wav")
  	img = cv2.imread("/content/drive/MyDrive/Project/face-without-mouth.jpg")
  	audio2mouth(audio_rate, audio_data)	