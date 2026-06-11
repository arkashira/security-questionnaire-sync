from flask import Flask
from sync import init_db, sync_endpoint

app = Flask(__name__)
init_db()  # create tables if they don't exist

app.add_url_rule('/sync', view_func=sync_endpoint, methods=['POST'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)