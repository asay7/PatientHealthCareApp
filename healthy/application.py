from flask import Flask
from .routes import homeBP, deviceBP, chatBP, userBP
import logging
import pymongo

application = Flask(__name__, instance_relative_config=False)
logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')

for handler in application.logger.handlers:
    application.logger.removeHandler(handler)

application.config.from_object('config.DevConfig')


'''
MONGO_URL = application.config["MONGO_URI"]

try:
    client = pymongo.MongoClient(host=MONGO_URL, serverSelectionTimeoutMS=2000)
    db = client.server_info()
    #only register the chat application if the server connection was successful, otherwise display an error
except:
    application.logger.error("Failed to connect to MongoDb server.")
'''

application.register_blueprint(userBP)
application.register_blueprint(deviceBP)

if __name__ == "main":
    application.run()
