from flask import Flask
from init import config

app = Flask(__name__)

if __name__ == "__main__":
    config()
    app.run()