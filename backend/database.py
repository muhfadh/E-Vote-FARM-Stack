from pydoc import doc
from typing import Collection
from model import Candidates

# MongoDB Driver
import motor.motor_asyncio 

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.Votes
collection = database.candidates


async def fetch_one_candidates(candidate_id):
    document = await collection.find_one({"candidate_id": candidate_id})
    return document

async def fetch_all_candidates():
    candidates = []
    cursor = collection.find({})
    async for document in cursor:
        candidates.append(Candidates(**document))
    return candidates