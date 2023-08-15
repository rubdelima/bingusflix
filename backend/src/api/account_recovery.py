from fastapi import APIRouter, HTTPException
from schemas.user import UserDB
from .users import database

router = APIRouter()