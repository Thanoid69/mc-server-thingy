import mcstatus
from mcstatus import JavaServer
import colorama 
from colorama import Fore, Back, Style
import os
os.system('mode con: cols=130 lines=30')

print(f"""{Fore.LIGHTRED_EX}
██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗     ██╗███████╗
██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║    ███║╚════██║
██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║    ╚██║    ██╔╝
╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║     ██║   ██╔╝ 
 ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║     ██║██╗██║  
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═╝╚═╝╚═╝  
                                                                       
 █████╗ ███╗   ██╗██████╗     ██╗   ██╗██████╗                         
██╔══██╗████╗  ██║██╔══██╗    ██║   ██║██╔══██╗                        
███████║██╔██╗ ██║██║  ██║    ██║   ██║██████╔╝                        
██╔══██║██║╚██╗██║██║  ██║    ██║   ██║██╔═══╝                         
██║  ██║██║ ╚████║██████╔╝    ╚██████╔╝██║                             
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═╝                             
                                                                       
 ██████╗ ███╗   ██╗██╗  ██╗   ██╗██╗                                   
██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝██║                                   
██║   ██║██╔██╗ ██║██║   ╚████╔╝ ██║                                   
██║   ██║██║╚██╗██║██║    ╚██╔╝  ╚═╝                                   
╚██████╔╝██║ ╚████║███████╗██║   ██╗                                   
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝   ╚═╝\n""")

ip = input(f"{Fore.RESET}IP and PORT ({Fore.YELLOW}Example{Fore.RESET}: 1.1.1.1:25565): ")

try:
    server = JavaServer.lookup(ip)
except Exception:
    print ("\nbro what")
    input()

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
    Players online: [{query.players.names}]
    Version: {status.version.name}
    Plugins: [{', ' .join(query.software.plugins)}]
    Motd: {query.motd}
    Map: {query.map}
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
            
            print('Query is disabled.')

lol()

input()
