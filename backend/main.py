from fastapi import FastAPI
from backend.api.dataset import router as dataset_router
from backend.api.query import router as query_router
from backend.api.insights import router as insights_router

app = FastAPI(title="AI Analytics Platform")

# Register routers
app.include_router(dataset_router, prefix="/api/dataset", tags=["Dataset"])
app.include_router(query_router, prefix="/api/query", tags=["Natural Query"])
app.include_router(insights_router, prefix="/api/insights", tags=["Insights"])

@app.get("/")
def read_root():
    return {"message": "AI Analytics Platform is running!"}