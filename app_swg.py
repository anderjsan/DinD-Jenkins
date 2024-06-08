from flask import Flask
from updater.updater import Updater
from updater.app_swagger import AppSwagger

if __name__ == "__main__":
    app = Flask(__name__)
    updater = Updater(app)
    swg = AppSwagger(app)
    
    updater.run()