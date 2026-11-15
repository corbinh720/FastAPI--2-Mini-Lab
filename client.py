
import typer
import requests
import json

app = typer.Typer()

BASE_URL = "http://127.0.0.1:8000"


@app.command()
def home():
    """Display the API welcome message."""
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        typer.echo(response.json())
    except requests.RequestException as e:
        typer.echo(f"Error: {e}")


@app.command()
def posts():
    """Get all posts from the FastAPI backend."""
    try:
        response = requests.get(
            f"{BASE_URL}/posts", timeout=10
        )
        response.raise_for_status()
        typer.echo(json.dumps(response.json(), indent=4))
    except requests.RequestException as e:
        typer.echo(f"Error: {e}")


@app.command()
def post(post_id: int):
    """Get a single post by ID."""
    try:
        response = requests.get(
            f"{BASE_URL}/posts/{post_id}", timeout=10
        )
        response.raise_for_status()
        typer.echo(json.dumps(response.json(), indent=4))
    except requests.RequestException as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
