import requests

LOADBALANCER_URL = "http://127.0.0.1:8089"
NUM_REQUESTS = 10

#Retrieves all registered servers from the loadbalancer
def get_servers():
    response = requests.get(f"{LOADBALANCER_URL}/servers")
    return response.json() if response.status_code == 200 else []


#Gets average response time to a given endpoint (in this case GameStorageNode)
def get_avg_response_time(url):
    times = [requests.get(url).elapsed.microseconds / 1000 for _ in range(NUM_REQUESTS)]
    for i, t in enumerate(times):
        print(f"Ping {i} took {t} ms")
    return sum(times) / NUM_REQUESTS

#Attempts to invoke /get-game from external server
def download_large_file(server_ip):
    file_url = f"{server_ip}/get-game"
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open("downloaded_large_file.dat", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Game downloaded successfully.")
    else:
        print("Game failed to download.")

#Retrieves all servers from LB, finds fastest, and attempts to download game
def main():
    if not (servers := get_servers()):
        return print("No servers available.")
    
    best_server = min(servers, key=lambda s: get_avg_response_time(s["ip"]))
    print(f"Fastest server: {best_server['name']} w. ip: {best_server['ip']}")
    
    download_large_file(best_server["ip"])

if __name__ == "__main__":
    main()