from fastapi import FastAPI
import pandas as pd

app = FastAPI()

NETFLIX_TITLES = pd.read_csv('netflix_titles.csv')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/titles")
async def titles():
    return NETFLIX_TITLES.fillna('').to_dict('records')
