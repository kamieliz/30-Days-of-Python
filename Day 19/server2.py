from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()

@app.get("/")
def hello_world():
    return {"hello": "world"}

@app.get("/box-office-mojo-scraper")
def scraper_runner_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1,2,3]}