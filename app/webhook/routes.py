from flask import Blueprint, json, request, jsonify, send_from_directory
from datetime import datetime
from app.extensions import collection
from app.scripts import format_event
from . import convert_timestamp
import os


webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    data = request.json
    
    print(f"data_: \n\n{data}\n\n\n\n\n{'#'*100}") 
    
    # Push event
    if 'commits' in data:
        timestamp= data["head_commit"]["timestamp"]
        event = {
            'action': 'push',
            'author': data['pusher']['name'],
            'to_branch': data['ref'].split('/')[-1],
            'timestamp': convert_timestamp(timestamp)
        }
        
    # PR event
    elif 'pull_request' in data and data['action']=="opened":
    # elif data.get('action')=="opened":
        event = {
            'action': 'pull_request',
            'author': data['pull_request']['user']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': convert_timestamp(data['pull_request']['created_at'])
        }
    
    # Merge event
    # elif 'merged' in data:
    elif 'pull_request' in data and data['pull_request']['merged']:
        import time
        print("Mergeddddddddddddddddddddd")
        time.sleep(4)
        event = {
            'action': 'merge',
            'author': data['pull_request']['merged_by']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': convert_timestamp(data['pull_request']['merged_at'])
        }
        
    else:
        return "Event not handled", 400

        
    collection.insert_one(event)
    print(f"EVENT INSERTED: {event}\n\n")
    return format_event(event), 200




