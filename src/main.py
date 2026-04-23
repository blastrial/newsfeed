from fastapi import FastAPI

app = FastAPI(title="NewsFeed API")


@app.get("/")
def home():
    return {
        "project": "NewsFeed",
        "message": "NewsFeed API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/version")
def version():
    return {
        "version": "0.1.0"
    }
