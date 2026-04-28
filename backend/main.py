import os
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from repositories import MockRepository, SQLRepository

load_dotenv()
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Mount the Local Image Folder
IMG_PATH = os.getenv("EXTERNAL_IMAGE_PATH", "./")
app.mount("/media", StaticFiles(directory=IMG_PATH), name="media")

BASE_MEDIA_URL = "http://localhost:8000/media"
DB_URL = os.getenv("DATABASE_URL")

repo = SQLRepository(DB_URL, BASE_MEDIA_URL) if DB_URL else MockRepository(BASE_MEDIA_URL)

@app.get("/api/categories")
def get_cats(): return repo.get_categories()

@app.get("/api/products")
def get_prods(category_id: int = Query(None)): return repo.get_products(category_id)