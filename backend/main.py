from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

NETFLIX_TITLES = pd.read_csv("netflix_titles.csv")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/titles")
async def titles(title: str = "", director: str = "", sortBy: str = ""):
    chosen_filter = pd.Series(True, index=range(0, len(NETFLIX_TITLES)))

    if title:
        chosen_filter &= NETFLIX_TITLES["title"].str.contains(title)

    if director:
        chosen_filter &= NETFLIX_TITLES["director"].fillna("").str.contains(director)

    selected = NETFLIX_TITLES[chosen_filter]
    if sortBy:
        selected = selected.sort_values(by=[sortBy])
        
    return selected.fillna("").to_dict("records")
