from fastapi import APIRouter
from api_v1.endpoints import calculation

api_router = APIRouter()

api_router.include_router(
    calculation.router,
    prefix=f"/math",
    tags=["Calculation"],
)