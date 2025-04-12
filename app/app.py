import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse-ip', methods=['GET'])
def reverse_ip():
    # Get the origin public IP from the request
    origin_ip = request.remote_addr
    if not origin_ip:
        return jsonify({"error": "Unable to determine IP address"}), 400

    # Reverse the IP address
    segments = origin_ip.split('.')
    reversed_ip = '.'.join(reversed(segments))
    return jsonify({"original_ip": origin_ip, "reversed_ip": reversed_ip})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Get the host and port from environment variables, with defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(host=host, port=port)