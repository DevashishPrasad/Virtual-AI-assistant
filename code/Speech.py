import speech_recognition as sr 
import time
import pyttsx3  
import sys  
sys.path.insert(0, 'flowtron')
sys.path.insert(0,'closed_domain')
import torch, gc
import flowAPI
from flowAPI import FlowAPI
from recordAudio import save_audio

class AI:
    def __init__(self):
        print("INIT")
        gc.collect()
        # torch.cuda.empty_cache()
        self.r = sr.Recognizer() 
        self.fp = flowAPI.FlowAPI()
        print("INTI DONE")

    def listen(self):
        try:
            # use the microphone as source for input
            audioFile = 'test.wav'
            save_audio(audioFile)
            userAudio = sr.AudioFile(audioFile)
            with userAudio as source2:   
                # self.r.adjust_for_ambient_noise(source2, duration=0.2) 
                #listens for the user's input  
                audio2 = self.r.record(source2)
                # Using google to recognize audio 
                query = self.r.recognize_google(audio2) 
                query = query.lower() 
                print("You : ",query)
                self.query = query
                print("[INFO] : Thinking, PLease wait")

        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
              
        except sr.UnknownValueError: 
            print("unknown error occured")
        finally:
        	pass

    def respond():

    def speak(self,text=None,SPEAKER_ID = 196):
        if text == None:
            text = self.reply          
         # 196 is a male voice & 1246 is a female voice
        self.fp.synthesize(speaker_id=1246,text=text)
        torch.cuda.empty_cache()

    # available speaker ids: 1069, 1088, 1116, 118, 1246, 125, 1263, 1502, 1578, 1841, 1867, 196, 1963, 1970, 200, 2092, 2136, 2182, 2196, 2289, 2416, 2436, 250, 254, 2836, 2843, 2911, 2952, 3240, 3242, 3259, 3436, 3486, 3526, 3664, 374, 3857, 3879, 3982, 3983, 40, 4018, 405, 4051, 4088, 4160, 4195, 4267, 4297, 4362, 4397, 4406, 446, 460, 4640, 4680, 4788, 5022, 5104, 5322, 5339, 5393, 5652, 5678, 5703, 5750, 5808, 587, 6019, 6064, 6078, 6081, 6147, 6181, 6209, 6272, 6367, 6385, 6415, 6437, 6454, 6476, 6529, 669, 6818, 6836, 6848, 696, 7059, 7067, 7078, 7178, 7190, 7226, 7278, 730, 7302, 7367, 7402, 7447, 7505, 7511, 7794, 78, 7800, 8051, 8088, 8098, 8108, 8123, 8238, 83, 831, 8312, 8324, 8419, 8468, 8609, 8629, 87, 8770, 8838, 887

A = AI()
A.listen()
# while (1):
# 	A.listen()
# 	print(A.query)
# 	A.speak(text = "I am manish. I like to see in the mirror. A lot.")
# 	print("Continue ?")
# 	if str(input()) == 'n':
# 		break
