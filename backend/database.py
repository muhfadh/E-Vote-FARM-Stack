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

async def create_candidates(candidates):
    document = candidates
    result = await collection.insert_one(document)
    return document

async def update_candidates(candidate_id, name, vision, mission):
    await collection.update_one(
        {"candidate_id": candidate_id}, 
        {"$set": {"name": name, "vision": vision, "mission": mission}})

    document = await collection.find_one({"candidate_id": candidate_id})

    return document

async def remove_candidates(candidate_id):
    try:
        await collection.delete_one({"candidate_id": candidate_id})
    except:
        return False
    return True

