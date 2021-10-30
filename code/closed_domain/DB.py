import sqlite3
import sys
import os

class Flight:
    def __init__(self,fromId,toId,airlineId,businessSeats,economySeats,businessFare,economyFare,arriveTime,departTime):
        self.fromId = fromId
        self.toId = toId
        self.airlineId = airlineId
        self.businessSeats = businessSeats
        self.economySeats = economySeats
        self.businessFare = businessFare
        self.economyFare = economyFare
        self.arriveTime = arriveTime
        self.departTime = departTime

    
    



def CREATE():
    os.system("rm atis.db")
    conn = sqlite3.connect('atis.db')
    print("Opened database successfully")

    # conn.execute('''DROP TABLE CITY''')
    # conn.execute('''DROP TABLE AIRPORT''')
    # conn.execute('''DROP TABLE AIRLINE''')
    # conn.execute('''DROP TABLE FLIGHT''')

    conn.execute('''CREATE TABLE CITY
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME           TEXT    NOT NULL);''')

    conn.execute('''CREATE TABLE AIRPORT
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            CITY_ID INTEGER NOT NULL,
            FOREIGN KEY (CITY_ID)
            REFERENCES CITY (ID));''')


    conn.execute('''CREATE TABLE AIRLINE
            (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
            NAME           TEXT    NOT NULL);''')


    conn.execute('''CREATE TABLE FLIGHT
            (
            ID INTEGER PRIMARY KEY     AUTOINCREMENT,
            FROM_ID         INTERGER NOT NULL,
            TO_ID           INTERGER NOT NULL,
            AIRLINE_ID           INTERGER NOT NULL,
            BUSINESS_SEATS  INT NOT NULL,
            ECONOMY_SEATS INT NOT NULL,
            BUSINESS_FARE REAL NOT NULL,
            ECONOMY_FARE REAL NOT NULL,
            ARRIVE_TIME TEXT NOT NULL,
            DEPART_TIME TEXT NOT NULL,
            FOREIGN KEY (FROM_ID) REFERENCES AIRPORT (ID),
            FOREIGN KEY (TO_ID) REFERENCES AIRPORT (ID),
            FOREIGN KEY (AIRLINE_ID) REFERENCES AIRLINE (ID)
            );''')

    print("Table created successfully")
    conn.close()
    
def INSERTCITY(city:str):
    conn = sqlite3.connect('atis.db')
    print("Opened database successfully")
    cursor = conn.cursor()
    
    sqlite_insert_query = """INSERT INTO CITY
                            (NAME) 
                            VALUES 
                            ('{}')""".format(city)
    print(sqlite_insert_query)
            
    count = cursor.execute(sqlite_insert_query)
    conn.commit()
    print("Record inserted successfully into CITY table ", cursor.rowcount)
    conn.close()

def INSERTAIRPORT(NAME:str,CITY_ID:int):
    try:    
        conn = sqlite3.connect('atis.db')
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO AIRPORT
                            (NAME, CITY_ID) 
                            VALUES 
                            ('{}',{})""".format(NAME,CITY_ID)

        count = cursor.execute(sqlite_insert_query)
        conn.commit()
        print("Record inserted successfully into AIRLINE table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
            

def INSERTAIRLINE(NAME:str):
    try:    
        conn = sqlite3.connect('atis.db')
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO AIRLINE
                            (NAME) 
                            VALUES 
                            ('{}')""".format(NAME)

        count = cursor.execute(sqlite_insert_query)
        conn.commit()
        print("Record inserted successfully into AIRPORT table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def INSERTFLIGHT(Object:Flight):
    try:    
        conn = sqlite3.connect('atis.db')
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO FLIGHT
                            (FROM_ID, TO_ID,AIRLINE_ID,BUSINESS_SEATS,ECONOMY_SEATS,BUSINESS_FARE,ECONOMY_FARE,ARRIVE_TIME,DEPART_TIME) 
                            VALUES 
                            ({},{},{},{},{},{},{},'{}','{}')""".format(Object.fromId,Object.toId,Object.airlineId,Object.businessSeats,Object.economySeats,Object.businessFare,Object.economyFare,Object.arriveTime,Object.departTime)

        count = cursor.execute(sqlite_insert_query)
        conn.commit()
        print("Record inserted successfully into FLIGHT table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
        if conn:
          conn.close()
        
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
            

            

# CREATE()
# INSERTAIRPORT("Orange Airport",1)


# INSERTAIRPORT("CSMI Airport",2)
# INSERTAIRPORT("MUMBAI AIRPORT",2)

# INSERTAIRPORT("Army Airport",3)

# INSERTAIRPORT("Idli Airport",4)

# INSERTAIRLINE("Air India")
# INSERTAIRLINE("Go Air")
# INSERTAIRLINE("Indigo")
# INSERTAIRLINE("King Fisher")



# (self,fromId,toId,airlineId,businessSeats,economySeats,businessFare,economyFare,arriveTime,departTime)

# nag2mum1 = Flight(fromId=1,toId=2,airlineId=1,businessSeats=10,economySeats=100,businessFare=2500,economyFare=1000,arriveTime="9:00 AM",departTime="7:00 AM")
# nag2mum2 = Flight(fromId=1,toId=2,airlineId=2,businessSeats=6,economySeats=50,businessFare=3000,economyFare=1500,arriveTime="9:00 PM",departTime="7:00 PM")

# pune2nag1 = Flight(fromId=4,toId=1,airlineId=2,businessSeats=6,economySeats=100,businessFare=530.6,economyFare=300.4,arriveTime='11:30 AM',departTime='9:00 AM')
# pune2nag2 = Flight(fromId=1,toId=4,airlineId=2,businessSeats=6,economySeats=100,businessFare=530.6,economyFare=300.4,arriveTime='01:30 PM',departTime='10:00 AM')

# pune2mum1 = Flight(fromId=4,toId=2,airlineId=3,businessSeats=6,economySeats=100,businessFare=530.6,economyFare=300.4,arriveTime='11:30 AM',departTime='10:00 AM')
# pune2mum2 = Flight(fromId=2,toId=4,airlineId=3,businessSeats=6,economySeats=100,businessFare=530.6,economyFare=300.4,arriveTime='01:30 PM',departTime='12:00 PM')

# che2mum1 = Flight(fromId=5,toId=3,airlineId=4,businessSeats=6,economySeats=100,businessFare=530.6,economyFare=300.4,arriveTime='03:30 PM',departTime='1:00 PM')
# mum2chen1 = Flight(fromId=3,toId=5,airlineId=4,businessSeats=6,economySeats=100,businessFare=530.6,economyFare=300.4,arriveTime='06:00 AM',departTime='3:00 AM')


pune2nag2 = Flight(fromId=1,toId=4,airlineId=1,businessSeats=10,economySeats=200,businessFare=2000.6,economyFare=100.4,arriveTime='02:30 PM',departTime='11:00 AM')
INSERTFLIGHT(pune2nag2)

pune2nag2 = Flight(fromId=1,toId=4,airlineId=3,businessSeats=12,economySeats=200,businessFare=1200.6,economyFare=800.4,arriveTime='03:30 PM',departTime='12:00 AM')
INSERTFLIGHT(pune2nag2)

pune2nag2 = Flight(fromId=1,toId=4,airlineId=4,businessSeats=4,economySeats=40,businessFare=35000.6,economyFare=2000.4,arriveTime='04:30 PM',departTime='1:00 AM')
INSERTFLIGHT(pune2nag2)

# INSERTFLIGHT(nag2mum1)
# INSERTFLIGHT(nag2mum2)

# INSERTFLIGHT(pune2mum1)
# INSERTFLIGHT(pune2mum2)

# INSERTFLIGHT(pune2nag1)
# INSERTFLIGHT(pune2nag2)

# INSERTFLIGHT(che2mum1)
# INSERTFLIGHT(mum2chen1)


'''
Nagpur -> Mumbai 7 AM
Nagpur -> Mumbai 7 PM



-----------Mumbai----------

Mumbai1 -> Nagpur 9 AM
Mumbai1 -> Nagpur 8 PM  


------------PUNE----------
Pune -> Nagpur 9 AM
Nagpur -> Pune 10 PM 
Pune -> Mumbai 10 AM
Mumbai -> Pune 12 PM


Chennai -> Mumbai(2) 1 PM
Mumbai(2)-> Chennai 3 AM

'''