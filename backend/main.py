from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async def get__all_candidates():
    return 1

@app.get("/api/candidates/{candidate_id}")
async def get_candidates_by_id(candidate_id):
    return 1

@app.post("/api/candidates")
async def create_candidates(candidates):
    return 1

@app.put("/api/candidates/{candidate_id}")
async def edit_candidates(candidate_id, candidates):
    return 1

@app.delete("/api/candidates/{candidate_id}")
async def delete_candidates(candidate_id):
    return 1
