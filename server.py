import socket
import os
from _thread import*

s = socket.socket()
ip = ('192.168.56.103')
port = 8000
ThreadCount = 0

s.bind((ip,port))

#output that show to input in client
s.listen(2000)
print(ip)
print(port)
print("\nWaiting for any incoming connections from client...\n")
print("\nPLEASE INPUT YOUR IP ADDRESS IN CLIENT !!")

#code that shows what file that are available
def threaded_client(connection):
	connection.send(str.encode('File available in server = add_two_number_python.py'))

#code that show server notices requested file
	while True:
		data = connection.recv(2048)
		reply = 'Server notice your requested file: '+data.decode('utf-8')
		if not data:
			break
		connection.sendall(str.encode(reply))
	connection.close()

#code that show the process of transmitting the files
while True:

	connect, addr = s.accept()
	print("-------------------------------------------------------")
	print('\nConnected to:'+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client, (connect, ))

	ThreadCount += 1
	print('Client Number: '+str(ThreadCount))

	filename = input(str("\nPlease enter the filename that need to be transmitted: "))
	file = open(filename , 'rb')
	file_data = file.read(1024)
	connect.send(file_data)
	print("Data has been transmited succesfully to client\n")

s.close()
