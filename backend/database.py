from model import Candidates, Votes

# MongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.Votes
collection = database.candidates

# =======================
# FOR CANDIDATES
# =======================
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

# =======================
# FOR VOTES
# =======================
collection_votes = database.votes
async def add_vote(votes):
    document = votes
    result = await collection_votes.insert_one(document)
    return document

async def count_votes_candidate_id(candidate_id):
    data = await collection_votes.count_documents({'candidate_id': {'$eq': candidate_id}})
    return data

async def count_total_votes():
    total_votes = await collection_votes.count_documents({})
    return total_votes


