import os
from typing import Optional, List

from fastapi import FastAPI, Body, HTTPException, status, Depends
from fastapi.responses import Response
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from enums import (
    RecosCategory,
    ShowCategory,
    BookCategory,
    MusicCategory,
    GameCategory,
    GamePlatform,
    AppCategory,
    Scopes,
    PodcastCategory,
)
from bson import ObjectId
import motor.motor_asyncio
from pymongo import ReturnDocument
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield db
    finally:
        client.close()


MONGO_URI = os.environ.get("MONGO_URI")


motor_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = motor_client.recos


async def get_db() -> motor_client:
    try:
        db = motor_client.recos
        yield db
    finally:
        client.close()


ouath2_app = FastAPI()
app = FastAPI()
