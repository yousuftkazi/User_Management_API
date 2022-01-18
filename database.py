import mysql.connector

db_config = {
    'host' :'localhost',
    'user' : 'root',
    'passwd' : 'root',
    'database': 'users'
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor()
