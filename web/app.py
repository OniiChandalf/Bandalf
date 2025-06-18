
import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from flask import Flask
from bot.db import get_all_users

app = Flask(__name__)

@app.route("/")
def home():
    return "Dashboard ist online!"
