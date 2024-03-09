from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query


app = FastAPI(
    title = "Fast API LMS",
    description = "LMS for managing students and courses",
    version = "0.0.1",
    contact = {
        "name": "Mash",
        "email": "mash@fastapi.co.za"
    },
    license_info = {
        "name" : "MIT",
    }
)

users =[]

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]
    test: str


@app.get("/users", response_model = List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return f'{user.email} added successfully'

@app.get("/users/{id}")
async def get_user(id: int = Path(..., description ="The ID for the user to be retrived", gt=2),
                   q: str = Query(None, max_length =5, description = "Field with Query Validation")
                   ):
    return {'user': users[id], "query": q}
