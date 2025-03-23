import subprocess
import re

server_au = "209.38.82.124"
server_nl = "174.138.14.43"

# Function to ping a server multiple times and extract response times
def ping_server(ip, count=100):
    # response = subprocess.run(["ping", "-c", str(count), ip], capture_output=True, text=True)
    response = subprocess.run(["ping", "-c", str(count), "-W", "5", ip], capture_output=True, text=True)
    print(response)
    times = re.findall(r'time[=<](\d+\.?\d+)', response.stdout)

    # times = re.findall(r'time=(\d+\.\d+)', response.stdout)
    print(times)
    return [float(time) for time in times]
# Ping both servers
audata = ping_server(server_au)
nldata = ping_server(server_nl)

with open("aus_data.txt", "w") as f:
    f.write("Sydney data\n")
    for i in audata:
        f.write(f"{i}\n")
with open("nld_data.txt", "w") as f:
    f.write("Amsterdam data\n")
    for i in nldata:
        f.write(f"{i}\n")


# Determine the closest server per sequence number
seq_numbers = list(range(1, len(audata) + 1))
closer_server = ["AU" if au < nl else "NL" for au, nl in zip(audata, nldata)]

# Write results to a file
with open("ping_results.txt", "w") as f:
    f.write("Seq_Num,AU_Ping,NL_Ping,Closer_Server\n")
    for seq, au, nl, closer in zip(seq_numbers, audata, nldata, closer_server):
        f.write(f"{seq},{au},{nl},{closer}\n")