from .. import schemas
from ..config import settings
from fastapi import status, HTTPException, APIRouter, Response
import requests

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Tasks']
)