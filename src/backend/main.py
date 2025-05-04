from fastapi import FastAPI
from .database import engine
from .models.post import Base
from .routers import posts

app = FastAPI(title = "Blog")

app.include_router(posts.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)