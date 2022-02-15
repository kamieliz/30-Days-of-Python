from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save

app = Flask(__name__)

# http://localhost:800/
@app.route("/", methods=['GET'])
def hello_world():
    # run other code here
    return "Hello, world. This is Flask"

@app.route("/box-office-mojo-scraper", methods=['POST'])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {'data': [1,2,3]}