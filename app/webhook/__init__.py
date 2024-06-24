from datetime import datetime
import pytz


def convert_timestamp(timestamp_str):
    timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    timestamp_utc = timestamp.astimezone(pytz.utc)
    formatted_timestamp = timestamp_utc.strftime('%d %B %Y - %I:%M %p UTC')
    day = int(formatted_timestamp.split(' ')[0])
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    formatted_timestamp = formatted_timestamp.replace(f'{day} ', f'{day}{suffix} ')
    return formatted_timestamp