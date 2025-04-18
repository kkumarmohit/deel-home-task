import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse-ip', methods=['GET'])
def reverse_ip():
    try:
        # Get the client's IP address from the X-Forwarded-For header
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        if x_forwarded_for:
            # Extract the first IP in the X-Forwarded-For list and remove the port (if present)
            client_ip = x_forwarded_for.split(',')[0].strip().split(':')[0]
        else:
            # Fallback to remote_addr if X-Forwarded-For is not present
            client_ip = request.remote_addr

        if not client_ip:
            return jsonify({"error": "Unable to determine client IP address"}), 400

        # Reverse the client's IP address
        segments = client_ip.split('.')
        reversed_ip = '.'.join(reversed(segments))
        return jsonify({"original_ip": client_ip, "reversed_ip": reversed_ip})
    except Exception as e:
        return jsonify({"error": "Failed to process IP", "details": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Get the host and port from environment variables, with defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(host=host, port=port)