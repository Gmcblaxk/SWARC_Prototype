from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_URL = "127.0.0.1"
AUS_URL = "209.38.82.124"
NDL_URL = "174.138.14.43"
EXPOSED_PORT = 5000
SERVERS = []

#Checks whether LoadBalancer can access external server
def check_server_availability(server):
    try:
        response = requests.get(server["ip"] + "/latency", timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
    
#API endpoint for GameStorageNode to register themselves w. LoadBalancer
@app.route('/register', methods=['POST'])
def register_server():
    data = request.json
    if "name" in data and "ip" in data:
        SERVERS.append({"name": data["name"], "ip": data["ip"]})
        return jsonify({"message": "Server registered successfully."}), 201
    return jsonify({"error": "Invalid data. Must contain 'name' and 'ip'."}), 400

#API endpoint for retrieving all available servers
@app.route('/servers', methods=['GET'])
def get_servers():
    available_servers = [server for server in SERVERS if check_server_availability(server)]
    return jsonify(available_servers)

if __name__ == '__main__':
    app.run(host="0.0.0.0")