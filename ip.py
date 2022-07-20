import geocoder
from colorama import *
import os
os.system('cls||clear')
print(f"""{Fore.GREEN}
██╗██████╗░░░░░░░████████╗██████╗░░█████╗░░█████╗░███████╗██████╗░
██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██████╔╝█████╗░░░██║░░░██████╔╝███████║██║░░╚═╝█████╗░░██████╔╝
██║██╔═══╝░╚════╝░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔══╝░░██╔══██╗
██║██║░░░░░░░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝███████╗██║░░██║
╚═╝╚═╝░░░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝


[1] Trace My Ip

[2] Trace Other Ip

{Fore.WHITE}""")
try:
	options = ["1", "2"]
	opt = input(f"{Fore.YELLOW}[-] Option {Fore.CYAN}: ")
	Fore.WHITE
	while opt not in options:
		print(f"{Fore.RED} Sorry. No option found")
		opt = input("[-] Re-enter the option : ")
	if (opt == "2"):
		ip = geocoder.ip(input(f"{Fore.YELLOW}[-] Enter the Ip Adress : {Fore.CYAN}"))
		Fore.WHITE
	print(f"{Fore.YELLOW}==================== {Fore.GREEN}[ Result ]{Fore.YELLOW} ===================={Fore.WHITE}")
	print("")
	if (opt == "1"):
		ip = geocoder.ip("me")
		json = ip.json
		for i in json:
			if (i != "raw"):
				print(Fore.GREEN+i+Fore.YELLOW+" : "+Fore.GREEN+str(json[i])+Fore.WHITE)
			else:
				for ii in json[i]:
					print(Fore.GREEN+ii+Fore.YELLOW+" : "+Fore.GREEN+str(json[i][ii])+Fore.WHITE)
		print("")
		print("")
		input("press enter to reboot")
		os.system("reboot.bat")
	elif (opt == "2"):
		json = ip.json
		for i in json:
			if (i != "raw"):
				print(Fore.GREEN+i+Fore.YELLOW+" : "+Fore.GREEN+str(json[i])+Fore.WHITE)
			else:
				for ii in json[i]:
					print(Fore.GREEN+ii+Fore.YELLOW+" : "+Fore.GREEN+str(json[i][ii])+Fore.WHITE)
		print("")
		print("")
		input("press enter to reboot")
		os.system("reboot.bat")
except KeyboardInterrupt:
	print(f"{Fore.RED}[!] Aborted process. rebooting!{Fore.WHITE}")
	os.system("reboot.bat")
