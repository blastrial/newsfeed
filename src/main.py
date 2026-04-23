from fastapi import FastAPI

app = FastAPI(title="NewsFeed API")

@app.get("/")
def root():
    return {"message": "NewsFeed API is running"}
