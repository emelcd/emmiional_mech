import os
from typing import Optional, List

from fastapi import FastAPI, Body, HTTPException, status, Depends
from fastapi.responses import Response
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from app.enums import (
    RecosCategory,
    Scopes,
)
from bson import ObjectId
import motor.motor_asyncio
from pymongo import ReturnDocument
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from app import app

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["reco"]


class User(BaseModel):
    email: EmailStr
    password: str
    scopes: List[Scopes] = []


class UserInDB(User):
    _id: str


class UserInResponse(BaseModel):
    _id: str
    email: EmailStr
    scopes: List[Scopes] = []


class Recommendation(BaseModel):
    title: str
    description: str
    category: RecosCategory


class RecommendationInDB(Recommendation):
    id: str
