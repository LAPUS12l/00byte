import os
from colorama import *
from hashlib import *
import hashlib
os.system("cls||clear")

print(f"""{Fore.BLUE}

██╗░░██╗░█████╗░░██████╗██╗░░██╗███████╗██████╗░  ░░██╗██████╗░
██║░░██║██╔══██╗██╔════╝██║░░██║██╔════╝██╔══██╗  ░██╔╝╚════██╗
███████║███████║╚█████╗░███████║█████╗░░██████╔╝  ██╔╝░░█████╔╝
██╔══██║██╔══██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗  ╚██╗░░╚═══██╗
██║░░██║██║░░██║██████╔╝██║░░██║███████╗██║░░██║  ░╚██╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░░╚═╝╚═════╝░
{Fore.WHITE}
""")
print(f"""{Fore.YELLOW}
[1] blake2b						[2] sha256

[3] blake2s						[4] sha384

[5] md5							[6] sha3_224

[7] sha1  						[8] sha3_256

[9] sha224 						[10] sha3_512

[11] sha512 						

{Fore.WHITE}

""")
hashes = {"1":"blake2b", "2":"sha256", "3":"blake2s", "4":"sha384", "5":"md5", "6":"sha3_224", "7":"sha1", "8":"sha3_256", "9":"sha224", "10":"sha3_512", "11":"sha512"}
opt = input(f"{Fore.YELLOW}[-] Enter your option :  {Fore.CYAN}: ")
while opt not in hashes:
	print(Fore.RED+"Invalid option"+Fore.WHITE)
	opt = input(f"{Fore.YELLOW}[-] Re-enter your option {Fore.CYAN}: ")
string = input(f"{Fore.YELLOW}[-] Enter word to encrypt :  {Fore.CYAN}: ")
if opt in hashes:
	res = eval(f"""hashlib.{hashes[opt]}(eval(f"b'"+string+"'")).hexdigest()""")
	print(f"{Fore.YELLOW}Result :{Fore.CYAN} "+res)
	print(Fore.WHITE+"")

input("press enter to reboot")
os.system("reboot")