import pyodbc
from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.ini")

driver = parser.get("SERVER_CONN", "DRIVER")
server = parser.get("SERVER_CONN", "SERVER")
database = parser.get("SERVER_CONN", "DATABASE")
username = parser.get("SERVER_CONN", "USERNAME")
password = parser.get("SERVER_CONN", "PASSWORD")

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()