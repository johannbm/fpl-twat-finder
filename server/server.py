from flask import Flask, send_from_directory

import asyncio
import fpl_helpers

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('../client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../client/public', path)

@app.route("/get-leauge-standings/<leauge_id>")
def get_leauge_standings(leauge_id):
    return asyncio.run(fpl_helpers.get_leauge_standings(leauge_id))

if __name__ == "__main__":
    app.run(debug=True)