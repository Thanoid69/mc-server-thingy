import mcstatus
from mcstatus import JavaServer

ip = input("IP and PORT (example; 111.1.111.111:25565): ")


server = JavaServer.lookup(ip)

status = server.status()

latency =  server.ping()

query = server.query()

print(f"{status.players.online} Players online. {status.latency} ms")
print(f"The server has the following players online: {', '.join(query.players.names)}")
print(f"Version: {'' .join(query.software.version)}")
print(f"Version: {'' .join(query.software.brand)}")
print(f"Plugins: {', ' .join(query.software.plugins)}")
print(f"Motd: {'' .join(query.motd)}")
print(f"Map: {'' .join(query.map)}")

input()
