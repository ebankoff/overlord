"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                      overlord                                   ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2022 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import re
import json
import time
import random
import ctypes
import requests
import datetime
import platform
from sys import exit
from time import sleep
from pathlib import Path
from sys import platform
from random import choice, randint
from colorama import Fore, Back, Style, init

proxy = []

with open(f"files/proxies.txt", "r", encoding="utf-8") as file:
	for line in file:
		proxy.append(line)

proxy = [line.rstrip() for line in proxy]


def check(file):
	try:
		global tokens
		global tokenFileName
		global checked
		global verified
		global unverified
		global sameTokens
		global invalid
		global nitro
		global idlist

		tokenFileName = f'files/{file}.txt'
		checkName = os.path.splitext(os.path.basename(tokenFileName))[0]

		dirValidTokens = f"files/{checkName}_valid.txt"
		dirParsedTokens = f"files/{os.path.basename(checkName)}_parsed.txt"

		checked = 0
		verified = 0
		unverified = 0
		sameTokens = 0
		invalid = 0
		nitro = 0
		idlist = []

		def main():
			try:
				global tokenFileName
				global found
				global tokens
				global tokenFileName
				global checked
				global verified
				global unverified
				global sameTokens
				global invalid
				global nitro
				global idlist

				print(f"Parsing tokens...")
				try:
					os.remove(dirParsedTokens)
				except: None
				global tokens
				tokens = []
				for line in [x.strip() for x in open(f"{tokenFileName}", errors="ignore").readlines() if x.strip()]:
					for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
						for token in re.findall(regex, line):
							tokens.append(token)
				tokens = list(dict.fromkeys(tokens))
				tokens_str = "\n".join(tokens)
				with open(dirParsedTokens, "a", encoding="utf-8") as f:
					f.write(tokens_str)
				found = len(open(dirParsedTokens).readlines())
				print()
				print(Fore.YELLOW + Style.BRIGHT + f"Found {Fore.CYAN}{found}{Fore.YELLOW + Style.BRIGHT} accounts")
				try:
					os.remove(dirDataTmp)
				except: None

				checker()

			except:
				pass

		def checker(): 
			global tokens
			global tokenFileName
			global checked
			global verified
			global unverified
			global sameTokens
			global invalid
			global nitro
			global idlist
			try:
				os.remove(dirValidTokens)
				os.remove(dirUnverifiedTokens)
				os.remove(dirInvalidTokens)
				os.remove(dirNitroTokens)
				os.remove(dirSameTokens)

			except: 
				pass

			try:
				for item in open(dirParsedTokens, "r").readlines():
					CheckToken(item.strip())

			except:
				pass

		def get_user_info(token: str):
			global tokens
			global tokenFileName
			global checked
			global verified
			global unverified
			global sameTokens
			global invalid
			global nitro
			global idlist
			proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
			json = requests.get("https://discordapp.com/api/v9/users/@me?verified", headers={"authorization": token}, proxies=proxies)
			time.sleep(.3)          
			if json.status_code == 200:
				json_response = json.json()
				if json_response["id"] not in idlist:
					idlist.append(json_response["id"])
					if json_response["verified"] == True:
						return True
					else:
						return False
				else:
					return "sameToken"
			else:
				return None

		def get_plan_id(token: str):
			global tokens
			global tokenFileName
			global checked
			global verified
			global unverified
			global sameTokens
			global invalid
			global nitro
			global idlist
			for json in requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers={"authorization": token}, proxies=proxies).json():
				try:            
					if json["plan_id"] == "511651880837840896":
						return True
					else:
						return False
				except:
					return None
				time.sleep(.3)

		def get_payment_id(token: str):
			global tokens
			global tokenFileName
			global checked
			global verified
			global unverified
			global sameTokens
			global invalid
			global nitro
			global idlist
			for json in requests.get("https://discordapp.com/api/v9/users/@me/billing/payment-sources", headers={"authorization": token}, proxies=proxies).json():
				try:
					if json["invalid"] == True:
						return True
					else:
						return False
				except:
					return None
				time.sleep(.3) 

		def CheckToken(token):
			try:
				global checked
				global verified
				global sameTokens
				global unverified
				global invalid
				global nitro
				if len(token) > 59:
					lenghtToken = f"{token}"
				else:
					lenghtToken = f"{token}"
				user_info = get_user_info(token)

				if user_info == "sameToken":
					print(f"{Fore.MAGENTA}{lenghtToken} | {Fore.BLUE}Identical token{Fore.RESET}")
					if platform == 'win32':
						ctypes.windll.kernel32.SetConsoleTitleW(f"{lenghtToken} | Identical token")
						
					sameTokens+= 1

				else:
					if user_info == None:
						if platform == 'win32':
							ctypes.windll.kernel32.SetConsoleTitleW(f"{lenghtToken} | Not working")
							
						print(f"{Fore.MAGENTA}{lenghtToken} | {Fore.RED}Not working{Fore.RESET}")

						invalid += 1

					elif user_info == True:
						if platform == 'win32':
							ctypes.windll.kernel32.SetConsoleTitleW(f"{lenghtToken} | Working")

						with open(dirValidTokens, "a", encoding="utf-8") as f:
							print(f"{Fore.MAGENTA}{lenghtToken} | {Fore.GREEN}Working{Fore.RESET}")
							f.write(token + "\n")

						verified += 1
						
					else:
						if platform == 'win32':
							ctypes.windll.kernel32.SetConsoleTitleW(f"{lenghtToken} | Working")

						with open(dirValidTokens, "a", encoding="utf-8") as f:
							print(f"{Fore.MAGENTA}{lenghtToken} | {Fore.GREEN}Working{Fore.RESET}")
							f.write(token + "\n")
						
						verified += 1

				checked  += 1

			except:
				pass

		main()

	except:
		pass