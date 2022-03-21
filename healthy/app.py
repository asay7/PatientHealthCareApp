from flask import Flask
from .routes import homeBP, deviceBP, chatBP, userBP
import logging
import pymongo

app = Flask(__name__, instance_relative_config=False)
logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')

for handler in app.logger.handlers:
    app.logger.removeHandler(handler)

app.config.from_object('config.DevConfig')


'''
MONGO_URL = app.config["MONGO_URI"]

try:
    client = pymongo.MongoClient(host=MONGO_URL, serverSelectionTimeoutMS=2000)
    db = client.server_info()
    #only register the chat app if the server connection was successful, otherwise display an error
except:
    app.logger.error("Failed to connect to MongoDb server.")
'''

app.register_blueprint(userBP)
app.register_blueprint(deviceBP)

if __name__ == "main":
    app.run()
