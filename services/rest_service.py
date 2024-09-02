from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

# Load peer configuration
with open('config/peer1_config.json') as f:
    config = json.load(f)

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(config['directory'])
    return jsonify(files)

if __name__ == '__main__':
    app.run(host=config['ip'], port=config['port'])
