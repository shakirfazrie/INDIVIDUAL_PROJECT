import socket
import os
from _thread import*

#code for entering server ip address
s = socket.socket()
ip = input(str("Please input your server IP address: "))
port = 8000
s.connect((ip,port))
print("Your server IP Address is successfully connected. Your server IP address is: "+ip)

respons = s.recv(1024)
print(respons)

#code for entering the filename that available on server
Input = input('\nPlease input the name file that you want from server: ')
s.send(str.encode(Input))
response = s.recv(1024)
print(response.decode('utf-8'))

#code for entering the filename of incoming file
filename = input(str("\nPlease enter a filename for the incoming file: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()

#code for showing that the file is recieved in client from server
print("File has been received succesfully.\n")

s.close()
