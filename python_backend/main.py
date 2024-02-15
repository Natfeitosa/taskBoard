from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def home():
    return {"Data" : "Testing"}

@app.get("/about")
def about():
    return {"About" : "help"}