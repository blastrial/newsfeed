from fastapi import FastAPI

app = FastAPI(title="NewsFeed API")


@app.get("/")
def read_root():
    return {"message": "NewsFeed API is running"}
