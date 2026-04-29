import os
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from db import init_db
from apps.catalog.routers import router as catalog_router
from repositories import MockRepository

load_dotenv()
app = FastAPI(title="Products and Surveys Catalog")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

from fastapi import Request
@app.middleware("http")
async def add_cache_control_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Mount the Local Image Folder
IMG_PATH = os.path.expanduser(os.getenv("EXTERNAL_IMAGE_PATH", "./"))
app.mount("/media", StaticFiles(directory=IMG_PATH), name="media")

BASE_MEDIA_URL = os.getenv("BASE_MEDIA_URL", "http://localhost:9999/media")
DB_URL = os.getenv("DATABASE_URL")

if DB_URL:
    init_db()
    app.include_router(catalog_router)
else:
    # Fallback to MockRepository
    repo = MockRepository(BASE_MEDIA_URL)
    
    @app.get("/api/categories")
    def get_cats(): return repo.get_categories()

    @app.get("/api/products")
    def get_prods(category_id: int = Query(None)): return repo.get_products(category_id)

# Mount the frontend application
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9999)