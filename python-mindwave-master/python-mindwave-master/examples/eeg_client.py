import socket
import sys
from itertools import cycle
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('172.20.10.2', 2222)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

output_short = cycle(range(100))
#output_boolean = cycle(range(2))
while True:
    #data = '#'+str(output_short.next())+str(output_boolean.next())+'@'
    data = str(output_short.next())+'\r\n'
    print data
    sock.sendall(data)
    sleep(0.5)
