from database import cursor, db
from models import User
from models import TVShow
from mysql.connector import errorcode
import json
import mysql.connector


def add_user(user: User):
    try:
        query = 'INSERT INTO users(id, name, favorite_tv_show) VALUES ("{}","{}","{}")'.format(user.id, str(user.name), str(user.favorite_tv_show.name))
        cursor.execute(query)
        db.commit()
        print("User created with id {}".format(user.id))
        return user
    except mysql.connector.Error as e:
        print(e)
        return False


def view_users():
    query = 'SELECT * FROM users ORDER BY id'
    cursor.execute(query)
    column_names=[x[0] for x in cursor.description]
    queryResult = cursor.fetchall()
    response = []
    for result in queryResult:
        response.append(dict(zip(column_names,result)))
    return response

def delete_user(userId: int):
    query = 'DELETE FROM users WHERE id={}'.format(userId)
    try:
        cursor.execute(query)
        db.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except mysql.connector.Error as e:
        print(e)
        return False


def update_user(userId:int ,user: User):
    query = 'UPDATE users SET id = {} , name = "{}", favorite_tv_show="{}" WHERE id={}'.format(user.id, str(user.name), str(user.favorite_tv_show.name),userId)
    cursor.execute(query)
    db.commit()
    print(cursor.fetchall())
    print("{} record(s) updated!".format(cursor.rowcount))
    return user
