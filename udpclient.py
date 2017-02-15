import socket
target_host = "localhost"
target_port = 22

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("AAABBBCCC",(target_host,target_port))
data,addr = client.recvfrom(4096)
print data