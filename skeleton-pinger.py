# HHHHHHHHH     HHHHHHHHH                                                                                                                                                     
# H:::::::H     H:::::::H                                                                                                                                                     
# H:::::::H     H:::::::H                                                                                                                                                     
# HH::::::H     H::::::HH                                                                                                                                                     
#   H:::::H     H:::::H      eeeeeeeeeeee  xxxxxxx      xxxxxxxppppp   ppppppppp   rrrrr   rrrrrrrrr       eeeeeeeeeeee        ssssssssss       ssssssssss      ooooooooooo   
#   H:::::H     H:::::H    ee::::::::::::ee x:::::x    x:::::x p::::ppp:::::::::p  r::::rrr:::::::::r    ee::::::::::::ee    ss::::::::::s    ss::::::::::s   oo:::::::::::oo 
#   H::::::HHHHH::::::H   e::::::eeeee:::::eex:::::x  x:::::x  p:::::::::::::::::p r:::::::::::::::::r  e::::::eeeee:::::eess:::::::::::::s ss:::::::::::::s o:::::::::::::::o
#   H:::::::::::::::::H  e::::::e     e:::::e x:::::xx:::::x   pp::::::ppppp::::::prr::::::rrrrr::::::re::::::e     e:::::es::::::ssss:::::ss::::::ssss:::::so:::::ooooo:::::o
#   H:::::::::::::::::H  e:::::::eeeee::::::e  x::::::::::x     p:::::p     p:::::p r:::::r     r:::::re:::::::eeeee::::::e s:::::s  ssssss  s:::::s  ssssss o::::o     o::::o
#   H::::::HHHHH::::::H  e:::::::::::::::::e    x::::::::x      p:::::p     p:::::p r:::::r     rrrrrrre:::::::::::::::::e    s::::::s         s::::::s      o::::o     o::::o
#   H:::::H     H:::::H  e::::::eeeeeeeeeee     x::::::::x      p:::::p     p:::::p r:::::r            e::::::eeeeeeeeeee        s::::::s         s::::::s   o::::o     o::::o
#   H:::::H     H:::::H  e:::::::e             x::::::::::x     p:::::p    p::::::p r:::::r            e:::::::e           ssssss   s:::::s ssssss   s:::::s o::::o     o::::o
# HH::::::H     H::::::HHe::::::::e           x:::::xx:::::x    p:::::ppppp:::::::p r:::::r            e::::::::e          s:::::ssss::::::ss:::::ssss::::::so:::::ooooo:::::o
# H:::::::H     H:::::::H e::::::::eeeeeeee  x:::::x  x:::::x   p::::::::::::::::p  r:::::r             e::::::::eeeeeeee  s::::::::::::::s s::::::::::::::s o:::::::::::::::o
# H:::::::H     H:::::::H  ee:::::::::::::e x:::::x    x:::::x  p::::::::::::::pp   r:::::r              ee:::::::::::::e   s:::::::::::ss   s:::::::::::ss   oo:::::::::::oo 
# HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeeexxxxxxx      xxxxxxx p::::::pppppppp     rrrrrrr                eeeeeeeeeeeeee    sssssssssss      sssssssssss       ooooooooooo   
#                                                              p:::::p                                                                                                       
#                                                              p:::::p                                                                                                       
#                                                             p:::::::p                                                                                                      
#                                                             p:::::::p                                                                                                      
#                                                             p:::::::p                                                                                                      
#                                                             ppppppppp   
#
#   _____ _        _      _                 __ _ _      
#  / ____| |      | |    | |               / _(_) |     
# | (___ | | _____| | ___| |_ ___  _ __   | |_ _| | ___ 
#  \___ \| |/ / _ \ |/ _ \ __/ _ \| '_ \  |  _| | |/ _ \
#  ____) |   <  __/ |  __/ || (_) | | | | | | | | |  __/
# |_____/|_|\_\___|_|\___|\__\___/|_| |_| |_| |_|_|\___|
#                                                       
                  
import time
from socket import *

# -=-=-=-=-=-=-=-=- Configuration -=-=-=-=-=-=-=-=-

ping_adres = "x"
ping_port = 00000
local_adres = ping_adres, ping_port

server_adres = "x"
server_port = 12001
remote_adres = server_adres, server_port

message = 'udp'

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
clientSocket.bind((local_adres))

message = message.encode("UTF-8")

counter = 1

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-

print('\n\n______________________\n   starting pinger.\n______________________')

while True:
    try:
        clientSocket.sendto(message, remote_adres)
        print('packet {} send.'.format(counter))
        flag, adres = clientSocket.recvfrom(1024)
        flag.decode('UTF-8')
        print('packet {} received.\n'.format(counter))
        
        counter += 1
    except:
        print('an error has occured, waiting 3 seconds.\n')

    time.sleep(3)
