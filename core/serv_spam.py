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


def getSuperProp(os, browser, useragent, browser_version, os_version, client_build):
    return {
        "os": os,
        "browser": browser,
        "device": "",
        "browser_user_agent": useragent,
        "browser_version": browser_version,
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": client_build,
        "client_event_source": None
    }


def generateUUID():
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	uuidlength = 32
	uuid = ""
	for i in range(uuidlength):
		uuid = uuid + alphabet[random.randrange(len(alphabet))]

	return uuid


def send2(token, trg, tm, rng):

	proxy = []

	with open("files/proxies.txt", "r", encoding="utf-8") as file:
		for line in file:
			proxy.append(line)

	proxy = [line.rstrip() for line in proxy]

	user_agent = ''
	cookie = f"__dcfduid={randstr(32)}; __sdcfduid={randstr(96)}; locale=ru; __cf_bm={randstr(189)}"
	os, browser, user_agent, browserver, osvers = getInfo()
	xsuperprop = base64.b64encode(json.dumps(getSuperProp(os, browser, user_agent, browserver, osvers, 36127), separators=",:").encode()).decode()

	mes = ""

	with open("files/message.txt", "r") as file:
		for line in file:
			mes += line

	st = 'payload = {"content":"","tts":False}'
	a1 = len(st) + len(mes)

	header = {
		"authorization": token,
		"accept": "*/*",
		'accept-encoding': 'gzip, deflate, br',
		"accept-language": "ru",
		"content-length": str(a1),
		"content-type": "application/json",
		"cookie": cookie,
		"origin": "https://discord.com",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"user-agent": user_agent,
		"x-debug-options": "bugReporterEnabled",
		"x-super-properties": xsuperprop
	}

	payload = {
		"content": mes,
		"tts": False
	}

	for t in range(rng):
		try:
			prx = random.choice(proxy)
			proxies = {'http': 'http://' + prx, 'https': 'http://' + prx}
			r = requests.post(f"https://discord.com/api/v9/channels/{trg}/messages", headers = header, json = payload, proxies = proxies)

			if r.status_code == 200 or r.status_code == 201:
				now = datetime.now()
				tm = str(now.strftime('%Y-%m-%d'))

				with open(f"log/log_servspam({tm}).txt", "a", encoding="utf-8") as file:
					file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'MESSAGE SENT' + '    |  ' + 'Target: ' + trg + '  |  ' + 'Token: ' + token + '\n')

				print(Fore.BLUE + "{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + Fore.WHITE + '  |  ' + Fore.GREEN + f'MESSAGE SENT' + Fore.WHITE + '    |  ' + Fore.CYAN + 'Target: ' + Fore.YELLOW + Style.BRIGHT + trg + Fore.WHITE + '  |  ' + Fore.CYAN + 'Token: ' + Fore.YELLOW + Style.BRIGHT + token)

				if platform == 'win32':
					ctypes.windll.kernel32.SetConsoleTitleW("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + ' | ' + f'MESSAGE SENT' + ' | ' + 'Target: ' + trg)

			else:
				now = datetime.now()
				tm = str(now.strftime('%Y-%m-%d'))

				with open(f"log/log_servspam({tm}).txt", "a", encoding="utf-8") as file:
					file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'MESSAGE FAILED' + '  |  ' + 'Target: ' + trg + '  |  ' + 'Token: ' + token + '\n')

				print(Fore.BLUE + "{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + Fore.WHITE + '  |  ' + Fore.RED + f'MESSAGE FAILED' + Fore.WHITE + '  |  ' + Fore.CYAN + 'Target: ' + Fore.YELLOW + Style.BRIGHT + trg + Fore.WHITE + '  |  ' + Fore.CYAN + 'Token: ' + Fore.YELLOW + Style.BRIGHT + token)

				if platform == 'win32':
					ctypes.windll.kernel32.SetConsoleTitleW("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + ' | ' + f'MESSAGE FAILED' + ' | ' + 'Target: ' + trg)

		except:
			pass

		time.sleep(tm)