from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/add")
def add(a:int, b:int) -> int:
    return a + b

@app.post("/subtract")
def subtract(a:int, b:int) ->int:
    return a - b

user_db ={
    1: {'name':'mirza', 'age':35},
    2: {'name':'Ali', 'age':25},
    3: {'name':'Hasan', 'age':63}
}

class user(BaseModel):
    name:str
    age:int

@app.put("/update")
def update_user(user_id:int, user:user):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message": f"User {user_id} updated", "user": user_db[user_id]}
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.delete("/delete")    
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
    else:
        print(f"User with user id {user_id} not found")
