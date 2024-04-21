from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Title": "Hello World"}
