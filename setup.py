import mysql.connector
from database import cursor
from mysql.connector import errorcode

DB = 'users'

TABLES ={}

TABLES['users'] = (
    "CREATE TABLE `users` ("
    " `id` int(10) NOT NULL,"
    " `name` varchar(25) NOT NULL,"
    " `favorite_tv_show` varchar(100) NOT NULL,"
    " PRIMARY KEY (`id`))"
)

def create_database():
    try:
        cursor.execute("CREATE DATABASE {}".format(DB))
        print ("{} database created successfully!".format(DB))
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_DB_CREATE_EXISTS:
                print('{} Database already exists'.format(DB))
        else:
            print(e.msg)


def create_tables():
    cursor.execute("USE {}".format(DB))
    for table in TABLES:
        createQuery = TABLES[table]
        try:
            cursor.execute(createQuery)
            print('{} table creted successfully'.format(table))
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('{} table already exists'.format(table))
            else:
                print(e.msg)

create_database()
create_tables()