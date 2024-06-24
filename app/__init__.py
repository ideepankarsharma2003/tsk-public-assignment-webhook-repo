from flask import Flask, jsonify, send_from_directory
import os
from app.webhook.routes import webhook
from .scripts import format_event
from .extensions import collection




# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    @app.route('/events', methods=['GET'])
    def get_events():
        # events = list(collection.find().sort('timestamp', -1))
        events = list(collection.find())
        formatted_events = [format_event(event) for event in events]
        return jsonify(formatted_events)

    @app.route('/')
    def index():
        directory = os.path.dirname(os.path.abspath(__file__))
        # print(f"list_dir: {os.listdir(directory)}")
        return send_from_directory(directory, 'index.html')

    
    return app
