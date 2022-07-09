import mcstatus
from mcstatus import JavaServer

ip = input("IP and PORT (example: 111.1.111.111:25565): ")


server = JavaServer.lookup(ip)

status = server.status()
latency =  server.ping()
query = server.query()

print(f"""\n{status.players.online} Players online. {status.latency} ms
The server has the following players online: {', '.join(query.players.names)}
Version: {'' .join(query.software.version)}
Version: {'' .join(query.software.brand)}
Plugins: {', ' .join(query.software.plugins)}
Motd: {'' .join(query.motd)}
Map: {'' .join(query.map)}
""")


input()
