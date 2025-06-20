import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from flask import Flask, render_template, request, redirect, url_for, session
from bot.db import get_all_users, mark_user_banned
from bot.config import ADMIN_PASSWORD
from bot.main import ban_user_on_discord, _loop

app = Flask(__name__)
app.secret_key = "supersecret"  # für Session-Management

@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    users = get_all_users()
    return render_template("dashboard.html", users=users)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["password"] == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/ban/<int:user_id>", methods=["POST"])
def ban_user(user_id):
    try:
        _loop.create_task(ban_user_on_discord(user_id))
    except Exception as e:
        print(f"❌ Fehler beim Discord-Bann: {e}")
    mark_user_banned(user_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
