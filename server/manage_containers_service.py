import os
import subprocess
import time
import requests
from flask import Flask, request, jsonify, session
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure random key

# Dictionary to track user containers
user_containers = {}

def get_or_create_user_id():
    """Get user ID from session or create a new one"""
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return session['user_id']

def wait_for_container(port, timeout=60):
    """Wait for the container to be ready by checking if the service responds"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Try to connect to the Jupyter server
            response = requests.get(f"http://127.0.0.1:{port}", timeout=5)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            # Container not ready yet, wait a bit
            time.sleep(2)
    return False

@app.route('/start', methods=['GET', 'POST'])
def start_container():
    # Get user ID from session
    user_id = get_or_create_user_id()
    
    # Check if the user already has a container
    if user_id in user_containers:
        port = user_containers[user_id]
        redirect_url = f"http://127.0.0.1:{port}"
        return '', 302, {'Location': redirect_url}

    # Find an available port (e.g., starting from 9000)
    base_port = 9000
    used_ports = user_containers.values()
    port = base_port
    while port in used_ports:
        port += 1

    # Start a new container for the user
    container_name = f"jupyter_{user_id}"
    command = [
        "docker", "run", "--rm", "-d",
        "--name", container_name,
        "-p", f"{port}:8888",
        "machine_learning_notes"
    ]
    
    try:
        subprocess.run(command, check=True)
        
        # Wait for the container to be ready
        if wait_for_container(port):
            # Save the container info
            user_containers[user_id] = port
            
            # Redirect to the container port
            redirect_url = f"http://127.0.0.1:{port}"
            return '', 302, {'Location': redirect_url}
        else:
            # Container failed to start within timeout
            subprocess.run(["docker", "stop", container_name], check=False)
            subprocess.run(["docker", "rm", container_name], check=False)
            return jsonify({"error": "Container failed to start within timeout"}), 500
            
    except subprocess.CalledProcessError:
        return jsonify({"error": "Failed to start container"}), 500


@app.route('/stop', methods=['POST'])
def stop_container():
    user_id = request.json.get('user_id')
    if not user_id or user_id not in user_containers:
        return jsonify({"error": "Invalid user ID"}), 400

    # Stop and remove the container
    container_name = f"jupyter_{user_id}"
    subprocess.run(["docker", "stop", container_name], check=True)
    subprocess.run(["docker", "rm", container_name], check=True)

    # Remove the user from the tracking dictionary
    del user_containers[user_id]
    return jsonify({"message": "Container stopped"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
