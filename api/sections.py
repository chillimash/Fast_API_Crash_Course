#from typing import Optional, List
import fastapi
# from pydantic import BaseModel
# from fastapi import FastAPI, Path, Query


router = fastapi.APIRouter()


@router.get("/Sections/{id}")
async def read_Sections():
    return {"Sections" : []}


@router.get("/Sections/{id}/contect-blocks")
async def read_section_contect_blocks():
    return {"Sections" : []}

@router.get("/contect-blocks/{id}")
async def read_contecnt_blocks():
    return {"sections" : []}