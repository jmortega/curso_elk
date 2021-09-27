#!/usr/bin/python
import socket
webhost = 'localhost'
webport = 8081
print("Contacting %s on port %d ..." % (webhost, webport))
webclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webclient.connect((webhost, webport))
webclient.send(bytes("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode('utf-8')))
reply = webclient.recv(4096)
print("Response from %s:" % webhost)
print(reply.decode())

import requests

url = 'http://localhost:8081'

my_data = {
    'message': 'this is the message'
}

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

response = requests.post(url, headers=headers,data=my_data['message'])
