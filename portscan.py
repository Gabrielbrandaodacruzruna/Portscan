#this is script is a sample portscan with python
#author: gabriel brandao da cruz runa
#version: 0.1




import socket #Libary for conection ip/tcp
import pyfiglet #libary for make a banner



ascii_banner = pyfiglet.figlet_format("PORT SCAN")
print(ascii_banner)
print("devolped by Gabriel brandao\n")

adress = raw_input("enter with the adress: ")



get_ip = socket.gethostbyname(adress)

for port in range(1,65325):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #way conetion to stream
    s.settimeout(0.2)  #set the time out
    result = s.connect_ex((adress,port)) #type of conetion 
    if result ==0: # condition like... if resulta its 200 is open 

        print get_ip, "-->", "is open" , "port", "--->", port  # result
