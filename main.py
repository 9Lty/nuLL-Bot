import os

# ... dein restlicher Code ...

def run_flask():
    # Holt sich den Port von Render, nutzt 8080 als Fallback für lokal
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
