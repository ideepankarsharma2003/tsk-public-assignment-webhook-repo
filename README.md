# Dev Assessment - Webhook Receiver

Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create the virtual env

```bash
python3 -m venv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

You need to use this as the base and setup the flask app. Integrate this with MongoDB (commented at `app/extensions.py`)

*******************

### Setting up MongoDB
```bash
sudo apt-get install gnupg curl

curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

sudo apt-get update

sudo apt-get install -y mongodb-org
```


### Starting MongoDB
```bash
sudo systemctl start mongod


(venv) ubuntu@ip-172-31-22-198:~/install$ sudo systemctl status mongod
● mongod.service - MongoDB Database Server
     Loaded: loaded (/usr/lib/systemd/system/mongod.service; disabled; preset: enabled)
     Active: active (running) since Mon 2024-06-24 07:36:09 UTC; 1min 6s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 180001 (mongod)
     Memory: 72.9M (peak: 73.5M)
        CPU: 1.106s
     CGroup: /system.slice/mongod.service
             └─180001 /usr/bin/mongod --config /etc/mongod.conf

Jun 24 07:36:09 ip-172-31-22-198 systemd[1]: Started mongod.service - MongoDB Database Server.
Jun 24 07:36:09 ip-172-31-22-198 mongod[180001]: {"t":{"$date":"2024-06-24T07:36:09.756Z"},"s":"I",  "c":"CONTROL",  "id":7484500, ">

(venv) ubuntu@ip-172-31-22-198:~/install$ 
```
----
