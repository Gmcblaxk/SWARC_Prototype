from flask import Flask, request, send_file, jsonify
import requests
import time
import argparse

app = Flask(__name__)

LOADBALANCER_URL = "http://127.0.0.1:8089/register"

BASE_URL = "127.0.0.1"

#Method to register itself with the LoadBalancer
def register_with_loadbalancer(port):
    server_info = {
        "name": str(port),
        "ip": f"http://localhost:{port}"
    }
    try:
        response = requests.post(LOADBALANCER_URL, json=server_info)
        if response.status_code == 201:
            print("Successfully registered with the load balancer.")
        else:
            print("Failed to register with the load balancer.")
    except requests.exceptions.RequestException:
        print("Could not reach the load balancer.")

#Dummy API endpoint used when getting latency benchmarks from client / loadbalancer
@app.route('/latency', methods=['GET'])
def check_latency():
    client_time = float(request.args.get('timestamp', time.time()))
    server_time = time.time()
    latency = server_time - client_time
    return jsonify({"latency": latency, "server_time": server_time})

#API endpoint to fetch a (semi-large) file from server
@app.route('/get-game', methods=['GET'])
def serve_large_file():
    file_path = "Component Diagram.drawio"  # Ensure this file exists in the same directory
    return send_file(file_path, as_attachment=True)

#On startup automatically registers itself w. loadbalancer (OBS remember arg "--port 8181" or similar)
def main():
    parser = argparse.ArgumentParser(description="Flask server with configurable port")
    parser.add_argument('--port', type=int, default=8180, help="Port to run the server on")
    args = parser.parse_args()
    
    register_with_loadbalancer(args.port)
    
    app.run(host='0.0.0.0')
    # app.run(host=BASE_URL, port=args.port, debug=False)

if __name__ == '__main__':
    main()
