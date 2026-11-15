
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(
    title="FastAPI 2 Mini-Lab",
    description="Public API Integration with Typer Client"
)

BASE_URL = "https://jsonplaceholder.typicode.com"


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI 2 Mini-Lab"}


@app.get("/posts")
def get_posts():
    try:
        response = requests.get(
            f"{BASE_URL}/posts", timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve posts"
        )


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    try:
        response = requests.get(
            f"{BASE_URL}/posts/{post_id}", timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            raise HTTPException(
                status_code=404,
                detail="Post not found"
            )

        return data
    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve post"
        )
