import socket
target_host = "10.113.14.163"
target_port = "9999"
target_port = int(target_port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP /1.1\r\nHost: google.com")
response = client.recv(4096)
print response