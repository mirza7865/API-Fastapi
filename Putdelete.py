from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db ={
    1: {'name':'mirza', 'age':35},
    2: {'name':'Ali', 'age':25},
    3: {'name':'Hasan', 'age':63}
}

class User(BaseModel):
    name:str
    age:int

@app.put("/update")
def update_user(user_id:int, user:BaseModel):
    if user_id in user_db:
        user_db[user_db] = user.todict()
        print(f'User details for {user_id} update :{user}')
    else:
        print(f"User {user_id} not found!")