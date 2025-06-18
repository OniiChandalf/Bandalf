
import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import threading
from bot.main import bot_thread
from web.app import app

t = threading.Thread(target=bot_thread, daemon=True)
t.start()

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
