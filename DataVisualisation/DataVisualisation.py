import matplotlib.pyplot as plt

# Server IPs
server_au = "209.38.82.124"
server_nl = "174.138.14.43"

# Load data from files
def load_ping_data(filename):
    with open(filename, "r") as f:
        return [float(line.strip()) for line in f]

audata = load_ping_data("aus_data.txt")
nldata = load_ping_data("nld_data.txt")

# Sequence numbers
seq_numbers = list(range(1, len(audata) + 1))
closer_server = ["AU" if au < nl else "NL" for au, nl in zip(audata, nldata)]

# Plot AU server pings
plt.figure(figsize=(12, 6))
plt.plot(seq_numbers, audata, marker='o', linestyle='-', label=f'Ping to {server_au}')
plt.xlabel("ICMP Sequence Number")
plt.ylabel("Ping Time (ms)")
plt.title("Ping Response Times - AU Server")
plt.legend()
plt.grid(True)
plt.savefig("ping_au.png")
plt.close()

# Plot comparison
plt.figure(figsize=(12, 6))
plt.plot(seq_numbers, audata, marker='o', linestyle='-', label='Ping to AU Server')
plt.plot(seq_numbers, nldata, marker='s', linestyle='-', label='Ping to NL Server')
plt.xlabel("ICMP Sequence Number")
plt.ylabel("Ping Time (ms)")
plt.title("Comparison of Ping Response Times")
plt.legend()
plt.grid(True)
plt.savefig("ping_comparison.png")
plt.close()

# Plot closer server decision
plt.figure(figsize=(12, 6))
plt.fill_between(seq_numbers, min(min(audata), min(nldata)), max(max(audata), max(nldata)), 
                 where=[s == "AU" for s in closer_server], color='blue', alpha=0.1, label='Closer to AU')
plt.fill_between(seq_numbers, min(min(audata), min(nldata)), max(max(audata), max(nldata)), 
                 where=[s == "NL" for s in closer_server], color='red', alpha=0.1, label='Closer to NL')
plt.xlabel("ICMP Sequence Number")
plt.ylabel("Ping Time (ms)")
plt.title("Closest Server Decision")
plt.legend()
plt.grid(True)
plt.savefig("ping_closer_server.png")
plt.close()

# Count occurrences
au_count = closer_server.count("AU")
nl_count = closer_server.count("NL")

# Categories and values
categories = ["AU", "NL"]
values = [au_count, nl_count]
colors = ["blue", "red"]

# Plot bar chart
plt.figure(figsize=(6, 6))
plt.bar(categories, values, color=colors, width=0.5)

# Labels and title
plt.xlabel("Server")
plt.ylabel("Count")
plt.title("Count of Closer Server Decisions")

# Save and show
plt.savefig("ping_closer_server_column.png")
plt.show()