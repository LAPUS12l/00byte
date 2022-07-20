
from colorama import *
import psutil
import os
import sys
from  pythonping import ping

scripts = [".iptracer", ".ddos", ".cal"]
susage = {".iptracer":"Trace Ip-Address Faster", ".ddos":"Ddos-Attacking tool", ".cal":"Calculator"}
#Functions
def res():
	return Fore.WHITE

#Initialize
os.system("cls")
ps = psutil.Process()

print(
f"""
{Fore.GREEN}
░█████╗░░█████╗░██████╗░██╗░░░██╗████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔════╝
██║░░██║██║░░██║██████╦╝░╚████╔╝░░░░██║░░░█████╗░░
██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╦╝░░░██║░░░░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝

{res()}""")
running = True
while running:
	command = input(">>>")
	if (command.lower() == ".cal"):
		import cal
	elif (command.lower() == ":reboot"):
		os.system("reboot.bat")
	elif (command == ".ddos"):
		import ddos.py
	elif (command[0:4] == "ping"):
		command = command.replace("ping", "", 1)
		while command[0:1] == " ":
			command = command.replace(" ", "", 1)
		print(ping(command))
	elif (command == ""):
		pass
	elif (command == "cls"):
		os.system('cls||clear')
	elif (command[0:2] == "-s"):
		command = command.replace("-s", "", 1)
		while command[0:1] == " ":
			command = command.replace(" ", "", 1)
		result = []
		for i in scripts:
			if command in i:
				result.append(i)
		for i in result:
			print("Result : ")
			print(i + " : "+susage[i])
	elif (command == ".hasher"):
		import hasher
	elif (command == ".python-v"):
		import pythonv
	elif (command == "reconfig"):
		os.system("cls||clear")
		print(
f"""
{Fore.GREEN}
░█████╗░░█████╗░██████╗░██╗░░░██╗████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔════╝
██║░░██║██║░░██║██████╦╝░╚████╔╝░░░░██║░░░█████╗░░
██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╦╝░░░██║░░░░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝

{res()}""")
	elif (command == ".iptracer"):
		import ip
	elif (command == "help"):
		print("""
Usage:
	For Scripts:
		-s <name>      Search Script

		-a             All Script
	Commands:
		.iptracer      Trace Ip-Address Faster

		.cal           Calculator

		.ddos          An free Ddos-Attacking tool
	System:
		ping           Ping a website

		reconfig       Reconfigure

		:reboot        Reboot the machine

	Authors:

		John Christian **  *******

		Contact : HTTPS://WWW.FACEBOOK.COM/SHISHIMINAMASAKI


""")

	else:
		print("Unknown command "+command)
