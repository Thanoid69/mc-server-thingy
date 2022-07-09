import mcstatus
from mcstatus import JavaServer



print("This tool is for version 1.7 and up.")

ip = input("IP and PORT (example: 111.1.111.111:25565): ")

mode = input("Select Mode  (1)Query Enabled (2)Query Disabled: ")

server = JavaServer.lookup(ip)

status = server.status()
latency =  server.ping()



def Query():
    try:    
        query = server.query()

        print(f"""
    Ping {status.latency} ms
    Player Slots: {status.players.max}
    Number of Players Online: {status.players.max}/{status.players.online}
    Players Online: [{', '.join(query.players.names)}]
    Version: {'' .join(query.software.version)}
    Version: {'' .join(query.software.brand)}
    Plugins: [{', ' .join(query.software.plugins)}]
    Motd: "{'' .join(query.motd)}"
    Map: {'' .join(query.map)}
        """)
    except Exception:
        print('Error, Not a Minecraft Server or has enable-query=false')

def Normal():
    try:
        print(f"""
    Ping {status.latency} ms
    Player Slots: {status.players.max}
    Number of Players Online: {status.players.max}/{status.players.online}
        """)
    except Exception:
        print('Error, Not a Minecraft Server')

if mode ==  "1":
    Query()

elif mode == "2":
    Normal()

else:
    print("Error, Invalid Mode.")

input()
