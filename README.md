# Architectural Prototype for Vapor


## How to run
1. Make sure you have the required python `flask` dependency. 
2. Start the LoadBalancer
```console
python3 LoadBalancer.py
```
3. Start any number of GameStorageNodes with 1 arg "port"
```console
python3 GameStorageNode/GameStorageNode.py --port 8181
```
4. Start the client and observe that it picks the fastest server and downloads a file
```console
python3 Client.py
```