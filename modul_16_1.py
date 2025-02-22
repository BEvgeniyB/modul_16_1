from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message":"hello"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message":"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def users(user_id:str) -> dict:
    return {"message":f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def users_info(user_name:str,age:int) -> dict:
    return {"message":f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"}