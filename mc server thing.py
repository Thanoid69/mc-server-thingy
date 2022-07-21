import mcstatus
from mcstatus import JavaServer



print("! This tool is for version 1.7 and up !\n")

ip = input("IP and PORT (example: 111.1.111.111:25565): ")


server = JavaServer.lookup(ip)

status = server.status()
latency =  server.ping()



def lol():
    try:    
        query = server.query()

        print(f"""
[    
    Ping: {status.latency} ms
    Player slots: {status.players.max}
    Number of players online: {status.players.online}/{status.players.max}
    Players online: [{', '.join(query.players.names)}]
    Version: {'' .join(query.software.version)}
    Version: {status.version.name}
    Plugins: [{', ' .join(query.software.plugins)}]
    Motd: {'' .join(query.motd)}"
    Map: {'' .join(query.map)}
[
        """)
    except Exception:
           
            try:
                print(f"""
    Ping: {status.latency} ms
    Player slots: {status.players.max}
    Number of Players online: {status.status.players.online}/{status.players.max}
    Version: {status.version.name}
[
                """)

            except Exception:
                print('Error, not a Minecraft server')
            
            print('Less info because the server has enable-query=false')

lol()

input()
