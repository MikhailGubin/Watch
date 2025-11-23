import asyncio
from schemas.user import User, UserCreate
from typing import List, Optional

#Временная база данных
users_db = [
    {"id": 1, "name": "Alice", "age": 24, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com"},
]

async def fetch_users() -> List[User]:
    return [User(**user) for user in users_db]

async def fetch_user_by_id(user_id: int) -> Optional[User]:
    for user in users_db:
        if user ["id"] == user_id:
            return User(**user)
        return None

async def add_user(user: UserCreate) -> Optional[User]:
    if any(u["email"] == user.email for u in users_db):
        return None
    new_id = max(user["id"] for user in users_db) + 1
    user_dict = user.dict()
    user_dict["id"] = new_id
    users_db.append(user_dict)
    return User(**user_dict)

async def delete_user(user_id: int) -> bool:
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index]
            return True
        return False
