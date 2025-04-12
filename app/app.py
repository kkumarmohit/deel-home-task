import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse-ip', methods=['GET'])
def reverse_ip():
    try:
        # Fetch the public IP using an external service
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        public_ip = response.json().get('ip')

        if not public_ip:
            return jsonify({"error": "Unable to determine public IP address"}), 400

        # Reverse the public IP address
        segments = public_ip.split('.')
        reversed_ip = '.'.join(reversed(segments))
        return jsonify({"original_ip": public_ip, "reversed_ip": reversed_ip})
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch public IP", "details": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Get the host and port from environment variables, with defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(host=host, port=port)