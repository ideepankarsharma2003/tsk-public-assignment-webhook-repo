
# For PUSH action:
    # Format: {author} pushed to {to_branch} on {timestamp}
    # Sample: "Travis" pushed to "staging" on 1st April 2021 - 9:30 PM UTC

# For PULL_REQUEST action:
    # Format: {author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}
    # Sample: "Travis" submitted a pull request from "staging" to "master" on 1st April 2021 - 9:00 AM UTC


# For MERGE action (Brownie Points):
    # Format: {author} merged branch {from_branch} to {to_branch} on {timestamp}
    # Sample: "Travis" merged branch "dev" to "master" on 2nd April 2021 - 12:00 PM UTC





def format_event(event):
    event_str= "Unknown event"
    if event['action'] == 'push':
        event_str= f"<b>{event['author']}</b> pushed to <b>{event['to_branch']}</b> on <b>{event['timestamp']}</b>"
    elif event['action'] == 'pull_request':
        event_str= f"<b>{event['author']}</b> submitted a pull request from <b>{event['from_branch']}</b> to <b>{event['to_branch']}</b> on <b>{event['timestamp']}</b>"
    elif event['action'] == 'merge':
        event_str= f"<b>{event['author']}</b> merged branch <b>{event['from_branch']}</b> to <b>{event['to_branch']}</b> on <b>{event['timestamp']}</b>"
    print(event_str)
    return event_str