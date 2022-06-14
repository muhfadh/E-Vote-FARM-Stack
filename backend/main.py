from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
    fetch_one_candidates,
    fetch_all_candidates,
    create_candidates, 
    update_candidates,
    remove_candidates
)
from model import Candidates


app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

@app.get("/")
def read_root():
    return {"Message": "Hello! "}

@app.get("/api/candidates")
async def get_all_candidates():
    response = await fetch_all_candidates()
    return response

@app.get("/api/candidates/{candidate_id}", response_model=Candidates)
async def get_candidates_by_id(candidate_id: int):
    response = await fetch_one_candidates(candidate_id)
    if response:
        return response
    raise HTTPException(404, f"There is no candidate with this candidate id: {candidate_id}")

@app.post("/api/candidates", response_model=Candidates)
async def post_candidates(candidates: Candidates):
    response = await create_candidates(candidates.dict())
    if response:
        return response
    raise HTTPException(400, f"Something went wrong or bad request :(")
    

@app.put("/api/candidates/{candidate_id}", response_model=Candidates)
async def put_candidates(candidate_id: int, name:str, vision: Union[str, None] = None, mission: Union[str, None] = None):
    response = await update_candidates(candidate_id, name, vision, mission)
    if response:
        return response
    raise HTTPException(404, f"There is no candidate with this candidate id: {candidate_id}")

@app.delete("/api/candidates/{candidate_id}")
async def delete_candidates(candidate_id: int):
    response = await remove_candidates(candidate_id)
    if response:
        return {"messages": f"Succesfully deleted candidates {candidate_id}"}
    raise HTTPException(404, f"There is no candidate with this candidate id: {candidate_id}")
    
