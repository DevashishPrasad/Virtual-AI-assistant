## List_flights

from collections import OrderedDict

dummy = {
  'FROM':'Pune',
  'TO':'Nagpur',
  'RESULTS':[
    {
      'ID':4129821, 
      'AIRLINE':'Indigo', 
      'B_SEATS':6,
      'E_SEATS':100,
      'B_FARE':530.6,
      'E_FARE':300.4,
      'ARRIVAL':'01:30 PM',
      'DEPARTURE':'12:00 PM'
    },
    {
      'ID':4129821, 
      'AIRLINE':'Indigo', 
      'B_SEATS':6,
      'E_SEATS':100,
      'B_FARE':530.6,
      'E_FARE':300.4,
      'ARRIVAL':'01:30 PM',
      'DEPARTURE':'12:00 PM'
    },
    {
      'ID':4129821, 
      'AIRLINE':'Indigo', 
      'B_SEATS':6,
      'E_SEATS':100,
      'B_FARE':530.6,
      'E_FARE':300.4,
      'ARRIVAL':'01:30 PM',
      'DEPARTURE':'12:00 PM'
    }
    ]
  }
dummy = OrderedDict(dummy)
## List_Capacity
dummy_cap = [
    {
      'FLIGHT_NO':4129821, 
      'B_SEATS':6,
      'E_SEATS':100
    },
    {
      'FLIGHT_NO':4129821, 
      'B_SEATS':6,
      'E_SEATS':100    },
    {
      'FLIGHT_NO':4129821, 
      'B_SEATS':6,
      'E_SEATS':100
    }
]

def prettify(text):
  text = str(text)
  text = text[:12]
  pad = (12 - len(text)) * " "
  text += pad
  return text

response = ""
def track_n_print(s):
  global response
  print(s)
  response += ' ' + s

def print_response(result, intent):
  global response
  response = ""
  
  print("\n[BOT] : ")
  track_n_print("Here are your results - ")
  if intent == "list_flights" or intent == "list_flight":
    # result = dummy
    if intent == "list_flights":
      track_n_print(f"I found {len(result['RESULTS'])} flights from {result['FROM']} to {result['TO']}")
    
    if len(result['RESULTS'])>0:
        header = result['RESULTS'][0].keys()
        print()
        for column in header:
            print(prettify(column), end='\t')
        
        for flight in result['RESULTS']:
          print()
          for key,value in flight.items():
            print(prettify(value), end='\t')
  else:
    track_n_print(f"I found {len(result)} results")
    if len(result) > 0:
        header = result[0].keys()
        print()
        for column in header:
            print(prettify(column), end='\t')

        for res in result:
          print()
          for key,value in res.items():
            print(prettify(value), end='\t')

    else:
        track_n_print("No record found !")
    
  return response
    
