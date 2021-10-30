from DB_manager import DB
from ResponseGenerator import print_response,dummy,dummy_cap
from collections import OrderedDict


"""
TODO 
1. Zero intend pe Sorry
"""



myDB = DB(db_file="closed_domain/atis.db")

def listFlights(slots:list,reply=True):
    
    fromLoc=None
    toLoc=None
    airline=None
    arriveTime=None
    departTime=None
    fromlocIsAirport=True
    tolocIsAirport=True
    Nothing = False
    
    for slot in slots:
        if slot[1] == 'flight_number':
            query = f"SELECT * FROM FLIGHT WHERE ID = {slot[0]};"
            result = myDB.executeQuery(query)
            result = myDB.insertAirlineName(result)
            dummy['RESULTS'] = format_dict(result)
            return print_response(dummy, "list_flight")

    for slot in slots:
        typeSlots = slot[1].split('.')
    
        if typeSlots[0] == "fromloc":
            if typeSlots[1][:4] == "city":
                fromlocIsAirport = False
            fromLoc=slot[0]
            
        if typeSlots[0] == "toloc":   
            if typeSlots[1][:4] == "city":
                tolocIsAirport = False
            toLoc=slot[0]
        
        if typeSlots[0] == "airline_name":
            airline = slot[0]
       

    query = "SELECT * FROM FLIGHT "

    # Bare min condition
    if((not fromLoc or not toLoc) and reply==True):
        print("Please also mention the Source and Destination in your query")
        return "Please also mention the Source and Destination in your query"
    elif((not fromLoc or not toLoc) and not reply):
        return [] 
    else:
        fromID = []
        toID = []
        if fromlocIsAirport:
            fromID.append(myDB.returnAirportIDByName(fromLoc))
        else: 
            f = myDB.cityIDByName(fromLoc)
            if len(f) == 0:
               Nothing = True  
            elif not Nothing:
                fromID = myDB.AirportByCityID(f[0])

        if tolocIsAirport:       
            toID.append(myDB.returnAirportIDByName(toLoc))
        else:    
            t = myDB.cityIDByName(toLoc)
            if len(t) == 0:
                Nothing = True  
            elif not Nothing:
                toID = myDB.AirportByCityID(t[0])
            
        if not Nothing:
            query += " WHERE FROM_ID = "+str(fromID[0])+" AND TO_ID = "+ str(toID[0])
            
        if len(toID) == 0 or len(fromID) == 0:
            Nothing = True   
   
    if airline and not Nothing:
        airline_id = myDB.returnAirlineIDByName(airline)
        query += " AND AIRLINE_ID = "+str(airline_id[0])

        # if len(airline_id) == 0:
        #     return []
    
    query += ';'
    # print(query)
    result = []
    if not Nothing:
        result = myDB.executeQuery(query)
    dummy['FROM'] = fromLoc
    dummy['TO'] = toLoc
    result = myDB.insertAirlineName(result)
    
    # Reponse
    if (reply):
     
      dummy['RESULTS'] = format_dict(result)
      return print_response(dummy, "list_flights")
    else:
      return result


def format_dict(result):
    
    result_dict = []
    
    for entry in result:
          dict_r = {
            'ID':entry[0], 
            'AIRLINE':entry[3], 
            'B_SEATS':entry[4],
            'E_SEATS':entry[5],
            'B_FARE':entry[6],
            'E_FARE':entry[7],
            'ARRIVAL':entry[8],
            'DEPARTURE':entry[9]
            }
          result_dict.append(dict_r)
          
    return result_dict
        
def fareFlights(slots:list):
    cost_relative = None # "ASD" = 0 and Des = 1
    class_type = None
    for typeSlots in slots:
    
        if typeSlots[1] == "cost_relative":
            if typeSlots[0].lower() == "minimum":
                cost_relative = "ASD"
            else:
                cost_relative = "DES"
            
        if typeSlots[1] == "class_type":   
            class_type = typeSlots[0].upper()+"_FARE"

    flights = listFlights(slots,reply=False)

    if len(flights) == 0:
        print("No flights Found")
        return "No flights Found"

    if class_type:
     	  if class_type[:8] == "BUSINESS":
            flights.sort(key=lambda i:i[6],reverse = (cost_relative == "DES"))
    else:
        flights.sort(key=lambda i:i[7],reverse = (cost_relative == "DES"))
    
    
    dummy['RESULTS']  = format_dict(flights)
    return print_response(dummy, "list_flights")
    # print("cost_relative",cost_relative)
    # print("class_type",class_type)
    # toLoc=slot[0]
            
def flightCapacity(slots):
    result = [] 
    flightNo = None
    
    for typeSlots in slots:
        if typeSlots[1] == "flight_number":
                flightNo = int(typeSlots[0]) 

    if flightNo:
        res = myDB.flightByID(flightNo)
        if len(res)>0:
            result.append(res)
    else:
        result = listFlights(slots,reply=False)
    
    dummy_cap = format_dict_capacity(result)
    return print_response(dummy_cap,"else")

def format_dict_capacity(result):
    
    result_dict = []
    
    for entry in result:
          dict_r = {
            'FLIGHT_NO':entry[0], 
            'B_SEATS':entry[4],
            'E_SEATS':entry[5]
            }
          result_dict.append(dict_r)
          
    return result_dict

      
query_dict = {
    "atis_flight":listFlights,
    "atis_airfare":fareFlights,
    "atis_quantity":flightCapacity,
    "atis_capacity":flightCapacity
    }

