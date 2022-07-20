import os
from colorama import *
os.system("cls")
print(f"""{Fore.GREEN}

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
{Fore.WHITE}""")
cal = True
while cal:
	print(f"""
[1] USING EXPRESSION

[2] ADDITION

[3] SUBTRACTION

[4] DIVISION

[5] MULTIPLICATION

""")
	opt = input("[-] Option : ")
	options = ["1", "2", "3", "4", "5"]
	while opt not in options:
		print(f"{Fore.RED}Sorry. Your option is invalid!{Fore.WHITE}")
		opt = input("[-] Please enter the correct option : ")
	if opt == "1":
		while cal:
			
			exp = str(input("[-] Enter the expression : "))
			if exp != "exit":
				print(f"{Fore.GREEN}[!] Result : {eval(exp)}{Fore.WHITE}")
			else:
				cal = False
	elif opt == "2":
		f = input("[-] Enter the first digit : ")
		s = input("[-] Enter the second difit : ")
		
		print(Fore.GREEN + "[!] Result : "+str(int(f) + int(s)))
		os.system("reboot.bat")
	elif opt == "3":
		f = input("[-] Enter the first digit : ")
		s = input("[-] Enter the second difit : ")
		
		print(Fore.GREEN + "[!] Result : "+str(int(f) - int(s))+Fore.WHITE)
		os.system("reboot.bat")
	elif opt == "4":
		f = input("[-] Enter the first digit : ")
		s = input("[-] Enter the second difit : ")
		
		print(Fore.GREEN + "[!] Result : "+str(int(f) / int(s))+Fore.WHITE)
		os.system("reboot.bat")
	elif opt == "5":
		f = input("[-] Enter the first digit : ")
		s = input("[-] Enter the second difit : ")
		
		print(Fore.GREEN + "[!] Result : "+str(int(f) * int(s))+Fore.WHITE)
		os.system("reboot.bat")
