import sqlite3
import sys
import os

class DB:
    
    def __init__(self,db_file="atis.db"):
        # print("Open")
        self.DB_NAME = db_file
        self.open()
        
    def open(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.DB_NAME)
        except Exception as e:
            print(e)
    
    def set_connection(self):
        
        
        return None
    
    def returnAirlineNameByID(self,airline_id:int):
        if self.conn == None:
            open()
        cur = self.conn.cursor()
        cur.execute("SELECT ID FROM AIRLINE WHERE NAME='{}' COLLATE NOCASE;".format(airline_id))
        rows = cur.fetchall()
        if len(rows)==0:
            return rows
        return rows[0][0] 
    
    def returnAirlineIDByName(self,airline_name:str):
        if self.conn == None:
            open()
        cur = self.conn.cursor()
        cur.execute("SELECT ID FROM AIRLINE WHERE NAME='{}' COLLATE NOCASE;".format(airline_name))
        rows = cur.fetchall()
        if len(rows)==0:
            return rows
        return rows[0]    

    def returnAirportIDByName(self,fromLoc:str):
        if self.conn == None:
            open()
        try:
            cur = self.conn.cursor()
            q = "SELECT ID FROM AIRPORT WHERE NAME='{}' COLLATE NOCASE;".format(fromLoc)
            cur.execute(q)
            rows = cur.fetchall()
            if len(rows)==0:
            	return rows
            return rows[0][0]
        except Exception as e:
            return None
        
    
    def AirportByCityID(self,city_id:int):
        if self.conn == None:
            open()
        cur = self.conn.cursor()
        cur.execute("SELECT ID FROM AIRPORT WHERE CITY_ID={}".format(city_id))
        rows = cur.fetchall()
        airports_in_city = []
        for airport in rows:
                airports_in_city.append(airport[0])
        return airports_in_city

    def cityIDByName(self,city_name:str):
        if self.conn == None:
            open()
        cur = self.conn.cursor()
        cur.execute("SELECT ID FROM CITY WHERE NAME='{}' COLLATE NOCASE;".format(city_name))
        rows = cur.fetchall()
        if len(rows)==0:
            return rows
        return rows[0]

    def flightByID(self,flight_id:int):
        if self.conn == None:
            open()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM FLIGHT WHERE ID='{}' COLLATE NOCASE;".format(flight_id))
        rows = cur.fetchall()
        if len(rows)==0:
            return rows
        return rows[0]

    # Execute raw query and return result 
    def executeQuery(self,query:str):
        if self.conn == None:
            open()
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows
        
    def insertAirlineName(self, result) :
        
        if self.conn == None:
            open()
                
        for i,row in enumerate(result):
            al_id=row[3]
            query = f"SELECT NAME FROM AIRLINE WHERE ID = {al_id};"
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            result[i] = list(result[i])
            result[i][3] = rows[0][0]
            

        return result
    
    def close(self):
        if not self.conn == None:
            self.conn.close()

    # Destructor
    def __del__(self):
        # print("Closing DB Connection")
        self.close()
      # body of destructor