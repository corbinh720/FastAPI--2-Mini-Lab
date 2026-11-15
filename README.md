
# FastAPI 2 Mini-Lab

# CIS 301 - Module 4 Assignment 2

# Project Description
This project demonstrates a FastAPI backend integrated
with a public API and a Typer command-line client.

# Technologies Used
- Python
- FastAPI
- Uvicorn
- Requests
- Typer
- JSONPlaceholder Public API

# Features
- Retrieve a welcome message
- Retrieve all posts from a public API
- Retrieve an individual post by ID
- Access endpoints using Swagger UI
- Interact with the backend using a Typer client

# Installation
pip install -r requirements.txt

# Run the FastAPI Server
uvicorn main:app --reload

# Run the Typer Client
Open a second terminal and run:

python client.py home

python client.py posts

python client.py post 1

# API Endpoints
GET /

GET /posts

GET /posts/{post_id}

# Testing
The FastAPI endpoints were tested using Swagger UI.

The Typer client provides commands to interact
with the FastAPI backend.
