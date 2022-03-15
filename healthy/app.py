from flask import Flask
from .routes import homeBP, deviceBP
import logging
import pymongo

app = Flask(__name__, instance_relative_config=False)

try:
    client = pymongo.MongoClient()
    db = client.users
except:
    print("error")

# logging.basicConfig(filename='app.log', level=logging.DEBUG)
app.config.from_object('config.DevConfig')

app.register_blueprint(homeBP)
app.register_blueprint(deviceBP)

if __name__ == "main":
    app.run()
