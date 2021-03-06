from typing import Union
from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import *
from model import Candidates, Votes


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
    db_user = await fetch_one_candidates(candidates.candidate_id)
    if db_user:
        raise HTTPException(400, f"candidate_id: {candidates.candidate_id} already in collection")

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

####################
@app.post("/api/votes", response_model=Votes)
async def vote_candidates(votes: Votes):
    response = await add_vote(votes.dict())
    if response:
        return response
    raise HTTPException(400, f"Something went wrong or bad request :(")

@app.get("/api/votes-count/{candidate_id}")
async def votes_count(candidate_id: int):
    response = await count_votes_candidate_id(candidate_id)
    if response:
        return {"candidate_id": candidate_id, "votes_count": response}
    raise HTTPException(404, f"There is no candidate with this candidate id: {candidate_id}")

@app.get("/api/total-votes")
async def get_total_votes():
    response = await count_total_votes()
    if response:
        return {"total_votes": response}

@app.get("/api/votes-result")
async def all_votes():
    response = await fetch_all_votes()
    return response
