from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/titles")
async def titles():
    return [{'title': 'Lorem ipsum', 'type': 'something', 'release_year': 2000}]
