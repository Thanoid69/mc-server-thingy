import mcstatus
from mcstatus import JavaServer
from discord_webhook import DiscordWebhook

hook = "https://discord.com/api/webhooks/989869264490070016/pX_zIV9xNM_2SQ5OkNvT3VEbbi9KvIaZHlM9uWaBsa6PSB_K4VHDyh5l7oYfAjiVZiRp"

print("! This tool is for version 1.7 and up !\n")

while 1 < 2:

    ip = input("IP and PORT (example: 111.1.111.111:25565): ")


    server = JavaServer.lookup(ip)

    status = server.status()
    latency =  server.ping()



    try:    
        query = server.query()

        cont = (f"""**Server info:**
    ```
        Ping {status.latency} ms
        Player slots: {status.players.max}
        Number of players online: {status.players.max}/{status.players.online}
        Players online: [{', '.join(query.players.names)}]
        Version: {'' .join(query.software.version)}
        Version: {'' .join(query.software.brand)}
        Plugins: [{', ' .join(query.software.plugins)}]
        Motd: {'' .join(query.motd)}"
        Map: {'' .join(query.map)}
    ```""")

    except Exception:
            
            try:
                cont2 = (f"""**Server info:**
    ```
        Ping {status.latency} ms
        Player slots: {status.players.max}
        Number of Players online: {status.players.max}/{status.players.online}
    ```""")

            except Exception:
                print('Error, not a Minecraft server')
                
            print('Less info because the server has enable-query=false')

    try:
        webhook = DiscordWebhook(url= hook, content= cont)
        response = webhook.execute()
    except Exception:
        webhook = DiscordWebhook(url = hook, content = cont2)
        response = webhook.execute()