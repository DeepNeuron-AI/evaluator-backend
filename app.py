from flask import Flask
from flask_cors import CORS
import config
import endpoints

APP_CONFIG = config.Config()

# Open and add json of config parameters
with open("config.json", "r") as f:
    APP_CONFIG.from_json(f.read())

# Launch app and add config parameters and endpoints
app = Flask(__name__)
app.config.update(APP_CONFIG.get_dict())
CORS(app, origins=app.config["CORS_ORIGINS"])
endpoints.register(app)

app.run()
