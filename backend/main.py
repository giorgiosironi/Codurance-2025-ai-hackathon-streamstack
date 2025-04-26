from fastapi import FastAPI
import pandas as pd

app = FastAPI()

NETFLIX_TITLES = pd.read_csv('netflix_titles.csv')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/titles")
async def titles(title: str = '', director: str = ''):
    if title:
        title_filter = NETFLIX_TITLES['title'].str.contains(title)
        return NETFLIX_TITLES[title_filter].fillna('').to_dict('records')
    if director:
        director_filter = NETFLIX_TITLES['director'].fillna('').str.contains(director)
        return NETFLIX_TITLES[director_filter].fillna('').to_dict('records')
    return NETFLIX_TITLES.fillna('').to_dict('records')
