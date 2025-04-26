from fastapi import FastAPI
import pandas as pd

app = FastAPI()

NETFLIX_TITLES = pd.read_csv("netflix_titles.csv")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/titles")
async def titles(title: str = "", director: str = ""):
    chosen_filter = pd.Series(True, index=range(0, len(NETFLIX_TITLES)))

    if title:
        chosen_filter = NETFLIX_TITLES["title"].str.contains(title)

    if director:
        chosen_filter = NETFLIX_TITLES["director"].fillna("").str.contains(director)

    return NETFLIX_TITLES[chosen_filter].fillna("").to_dict("records")
