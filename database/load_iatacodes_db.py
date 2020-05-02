import json
import sqlite3

input_file = open("airport-codes_json.json")
json_array = json.load(input_file)

# Creating the database to load the iata codes into it

# Database lives in memory
# Easy for testing
# Starts completly fresh
# file saved as db.db
conn = sqlite3.connect('airport_iata.db')
c = conn.cursor()

# Creates the iata_code table 
c.execute("""CREATE TABLE iata_code (
            airport text,
            code text
            )""")

# For loop that will go through the json file 
# Sorts all of the continents by the NA (North America)
for item in json_array:
    if item['continent'] == 'NA':
        # Convers the 'iata_code' json type to a string
        iata_code_str = item['iata_code']
        # convers the 'name' json type to a string 
        airport_name_str = item['name']
        # inserts the airport name and the iata code into the database
        c.execute("INSERT INTO iata_code VALUES (:airport, :code)", {'airport': airport_name_str, 'code': iata_code_str})
        
conn.commit()

conn.close()