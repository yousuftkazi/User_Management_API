from fastapi import FastAPI, HTTPException
from models import User
import controller as orm

app = FastAPI()

@app.get('/users')
async def getUsers():
    users = orm.view_users()
    return {'users' : users}

@app.post('/users/create')
async def createUser(user: User):
    user = orm.add_user(user)
    if user:
        return {"user":user}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error. Check your inputs, user with this id could already exists")
 
@app.delete('/users/delete/{userId}')
async def deleteUser(userId: int):
    if orm.delete_user(userId):
        return "Successfully Deleted"
    else:
        raise HTTPException(status_code=404, detail="Error while deleting. Check user Id")

@app.post('/users/update/{userId}')
async def updateUser(userId:int, user: User):
    orm.update_user(userId,user)
    return {'user' : user}