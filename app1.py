from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "updated Flask sample application on azure hghapp service updated verrsion-4"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
