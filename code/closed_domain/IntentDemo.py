'''
ATIS FLIGHT
ATIS FARE 
ATIS CAPACITY
'''
import sys
import warnings
from pprint import pprint
from predict import Predictor
sys.path.append('/content/drive/MyDrive/Project/AHC_Integrated/Integrated/closed_domain')
from ReplyHelper import *

import os

# clear = lambda: os.system('clear')

class IntentReply:
    
    def __init__(self):
        self.model = Predictor()
        # clear()

    def predict(self,query):
        ans = self.model.predict(query)
        self.intent = ans[0]
        self.slots = ans[1]

    def reply(self):
            pass

    def __call__(self, query):
        self.predict(query)
        self.reply()
        result = []
        if(str(self.intent) == "atis_abbreviation"):
            print("[BOT] : I am afraid, I can not understand your query. Can you please restructure your query?")
            return "I am afraid, I can not understand your query. Can you please restructure your query?"
        else:
            if self.intent in query_dict.keys(): 
              return query_dict[self.intent](self.slots)
            else:
              return "I am afraid, I can not understand your query. Can you please restructure your query?"

# IR = IntentReply()

# while(True):
# 	query = input("[USER] : ")
# 	if query.lower() == "exit" or query.lower() == "bye" :
# 		print("[BOT] : Bye, Have a Nice day ")
# 		break
# 	IR(query)   