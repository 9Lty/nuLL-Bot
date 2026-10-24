import os
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "Online"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
