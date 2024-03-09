# from typing import Optional, List
import fastapi
# from pydantic import BaseModel
# rom fastapi import FastAPI, Path, Query


router = fastapi.APIRouter()

@router.get("/courses")
async def get_courses():
    return {"courses" : []}

@router.post("/courses")
async def create_course():
    return {"course" : []}

@router.get("/courses/{id}")
async def get_user(id: int):
    return {'courses': []}

@router.patch("/courses/{id}")
async def update_sourse():
    return {'courses': []}

@router.delete("/courses/{id}")
async def delete_sourse():
    return {'courses': []}