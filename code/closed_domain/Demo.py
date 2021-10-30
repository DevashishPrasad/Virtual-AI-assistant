from predict import Predictor
import warnings
warnings.filterwarnings("ignore")

class IntendReply:

	def __init__(self):

		self.model = Predictor()

	def predict(self,query):
		ans = self.model.predict(query)
		self.intend = ans[0]
		self.slots = ans[1]

	def reply(self):
		pass

	def __call__(self, query):
		self.predict(query)
		self.reply()
		print(self.intend)
		print(self.slots)

IR = IntendReply()

IR("Book a flight from delhi Airport to CSMI of AirIndia")