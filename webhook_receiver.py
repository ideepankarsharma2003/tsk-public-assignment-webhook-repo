from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['webhook_db']
collection = db['events']

def format_event(event):
    if event['action'] == 'push':
        return f"{event['author']} pushed to {event['to_branch']} on {event['timestamp']}"
    elif event['action'] == 'pull_request':
        return f"{event['author']} submitted a pull request from {event['from_branch']} to {event['to_branch']} on {event['timestamp']}"
    elif event['action'] == 'merge':
        return f"{event['author']} merged branch {event['from_branch']} to {event['to_branch']} on {event['timestamp']}"
    return "Unknown event"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'commits' in data:
        # Push event
        event = {
            'action': 'push',
            'author': data['pusher']['name'],
            'to_branch': data['ref'].split('/')[-1],
            'timestamp': datetime.utcnow()
        }
    elif 'pull_request' in data:
        # Pull request event
        event = {
            'action': 'pull_request',
            'author': data['pull_request']['user']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': datetime.utcnow()
        }
    elif 'merged' in data:
        # Merge event
        event = {
            'action': 'merge',
            'author': data['pull_request']['merged_by']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': datetime.utcnow()
        }
    else:
        return "Event not handled", 400

    collection.insert_one(event)
    return format_event(event), 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort('timestamp', -1).limit(10))
    formatted_events = [format_event(event) for event in events]
    return jsonify(formatted_events)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
