import sqlite3

try:
     mi_conexion = sqlite3.connect("database")      
except Exception as ex: 
     print(ex)     


    