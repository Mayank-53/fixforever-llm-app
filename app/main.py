from fastapi import FastAPI
from app.routers import issue_router

app = FastAPI(title="FixForever Issue Resolver API")

app.include_router(issue_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to FixForever LLM API"}