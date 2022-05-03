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
import sys
import time
import json
import emoji
import random
import shutil
import socket
import ctypes
import smtplib
import os.path
import asyncio
import requests
import colorama
import datetime
import threading
import user_agent
import progressbar
from time import sleep
from threading import *
from sys import platform
from asyncio import sleep
from getpass import getpass
from os import name, system
from progress.bar import Bar
from threading import Thread
from functools import reduce
from requests import get, post
from os.path import exists, isfile
from random import choice, randint
from progress.spinner import Spinner
from colorama import Fore, Back, Style, init

colorama.init()


def randstr(lenn):
	lib = "abcdefghijklmnopqrstuvwxyz0123456789"
	text = ''
	for i in range(0, lenn):
			text += lib[random.randint(0, len(lib) - 1)]
	return text


def getInfo():
	id = random.randint(1, 15)
	if id == 1:
		return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36", "69.0.3497.100", "10.0")
	elif id == 2:
		return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "18.17763", "10.0")
	elif id == 3:
		return ("Windows", "Edge", "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36", "60.0.3112.90", "5.1")
	elif id == 4:
		return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", "60.0.3112.113", "8.1")
	elif id == 5:
		return ("Windows", "Internet Explorer", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko", "11.0", "10.0")
	elif id == 6:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0", "54.0", "6.1")
	elif id == 7:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "66.0", "10.0")
	elif id == 8:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.1; rv:94.0) Gecko/20100101 Firefox/94.0", "94.0", "6.1")
	elif id == 9:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:94.0) Gecko/20100101 Firefox/94.0", "94.0", "6.1")
	elif id == 10:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0", "90.0", "6.3")
	elif id == 11:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "92.0", "6.3")
	elif id == 12:
		return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0", "89.0", "6.3")
	elif id == 13:
		return ("Windows", "Chrome", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36", "93.0.4577.63", "10.0")
	elif id == 14:
		return ("Windows", "Opera", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56", "79.0.4143.56", "6.3")
	elif id == 15:
		return ("Windows", "Opera", "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4719.208 Safari/537.36 OPR/80.0.2303.183", "80.0.2303.183", "11_4")


def send1(token, trg, tm, rng):

	proxy = []

	with open(f"files/proxies.txt", "r", encoding="utf-8") as file:
		for line in file:
			proxy.append(line)

	proxy = [line.rstrip() for line in proxy]

	try:
		mes = ""

		with open("files/message.txt", "r") as file:
			for line in file:
				mes += line

		for t in range(rng):
			prx = random.choice(proxy)
			user_agent = ''
			proxies = {'http': 'http://' + prx, 'https': 'http://' + prx}
			os, browser, user_agent, browserver, osvers = getInfo()

			pld = '''{'recipient_id':""}'''
			lng = len(pld) + len(trg)

			header = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
				'authorization': token,
				'content-length': str(lng),
				'content-type': 'application/json',
				'cookie': '__dcfduid=1ba56720a9a711ecb19c2180452a5394; __sdcfduid=1ba56721a9a711ecb19c2180452a53943eefaff20fa4fabba0a4df53e085d4d8cd1e01df8a2ed6be8f0d96b97542bb6d; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+01+2022+16%3A37%3A33+GMT%2B0300+(Moscow+Standard+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; __cf_bm=hIJra_8RJKMUjQbECoop68Nadg26AJj21O.8YjnHanw-1648823657-0-AZR/d7z8u3Ia1M0v60GkpTK2hvHRPw11AaWzaJNEB1CS2Ln3cPeuucb9GXu6xRcVpjFSFybaGcMUuv3XV9ux+4QF5gjs6WqdFerHiTh5xzFvcL41aQgP/AmV/0glSH1U7A==; locale=en-US',
				'origin': 'https://discord.com',
				'referer': f'https://discord.com/channels/@me/{trg}',
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'user-agent': user_agent,
				'x-debug-options': 'bugReporterEnabled',
				'x-discord-locale': 'en-US',
				'x-kl-ajax-request': 'Ajax_Request',
				'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InJ1LVJVIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMC4wLjQ4OTYuNjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMC4wLjQ4OTYuNjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTIxNzE5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
			}

			payload = {'recipient_id': trg}
			r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers = header, json = payload, proxies = proxies)
			j = json.loads(r1.content)

			pld = '{"content":"","tts":False}'
			lng = len(pld) + len(msg)

			payload = {"content":mes,"tts":False}

			header = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
				'authorization': token,
				'content-length': str(lng),
				'content-type': 'application/json',
				'cookie': '__dcfduid=1ba56720a9a711ecb19c2180452a5394; __sdcfduid=1ba56721a9a711ecb19c2180452a53943eefaff20fa4fabba0a4df53e085d4d8cd1e01df8a2ed6be8f0d96b97542bb6d; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+01+2022+16%3A37%3A33+GMT%2B0300+(Moscow+Standard+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; __cf_bm=hIJra_8RJKMUjQbECoop68Nadg26AJj21O.8YjnHanw-1648823657-0-AZR/d7z8u3Ia1M0v60GkpTK2hvHRPw11AaWzaJNEB1CS2Ln3cPeuucb9GXu6xRcVpjFSFybaGcMUuv3XV9ux+4QF5gjs6WqdFerHiTh5xzFvcL41aQgP/AmV/0glSH1U7A==; locale=en-US',
				'origin': 'https://discord.com',
				'referer': f'https://discord.com/channels/@me/{trg}',
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'user-agent': user_agent,
				'x-debug-options': 'bugReporterEnabled',
				'x-discord-locale': 'en-US',
				'x-kl-ajax-request': 'Ajax_Request',
				'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InJ1LVJVIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMC4wLjQ4OTYuNjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMC4wLjQ4OTYuNjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTIxNzE5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
			}
			
			r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages", headers = header, json = payload, proxies = proxies)

			if r2.status_code == 200 or r2.status_code == 201:
				now = datetime.now()
				tm = str(now.strftime('%Y-%m-%d'))

				with open(f"log/log_dmspam({tm}).txt", "a", encoding="utf-8") as file:
					file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'MESSAGE SENT' + '    |  ' + 'Target: ' + trg + '  |  ' + 'Token: ' + token + '\n')

				print(Fore.BLUE + "{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + Fore.WHITE + '  |  ' + Fore.GREEN + f'MESSAGE SENT' + Fore.WHITE + '    |  ' + Fore.CYAN + 'Target: ' + Fore.YELLOW + Style.BRIGHT + trg + Fore.WHITE + '  |  ' + Fore.CYAN + 'Token: ' + Fore.YELLOW + Style.BRIGHT + token)

				if platform == 'win32':
					ctypes.windll.kernel32.SetConsoleTitleW("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + ' | ' + f'MESSAGE SENT' + ' | ' + 'Target: ' + trg)

			else:
				now = datetime.now()
				tm = str(now.strftime('%Y-%m-%d'))

				with open(f"log/log_dmspam({tm}).txt", "a", encoding="utf-8") as file:
					file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'MESSAGE FAILED' + '  |  ' + 'Target: ' + trg + '  |  ' + 'Token: ' + token + '\n')

				print(Fore.BLUE + "{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + Fore.WHITE + '  |  ' + Fore.RED + f'MESSAGE FAILED' + Fore.WHITE + '  |  ' + Fore.CYAN + 'Target: ' + Fore.YELLOW + Style.BRIGHT + trg + Fore.WHITE + '  |  ' + Fore.CYAN + 'Token: ' + Fore.YELLOW + Style.BRIGHT + token)

				if platform == 'win32':
					ctypes.windll.kernel32.SetConsoleTitleW("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + ' | ' + f'MESSAGE FAILED' + ' | ' + 'Target: ' + trg)
				
			time.sleep(tm)

	except:
		pass