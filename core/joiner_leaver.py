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
import base64
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
from anticaptchaofficial.hcaptchaproxyless import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

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


def generateUUID():
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	uuidlength = 32
	uuid = ""
	for i in range(uuidlength):
		uuid = uuid + alphabet[random.randrange(len(alphabet))]

	return uuid


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


def join1(token, invite, key):
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	user_agent = ''
	proxy = []

	with open(f"files/proxies.txt", "r", encoding="utf-8") as file:
		for line in file:
			proxy.append(line)

	proxy = [line.rstrip() for line in proxy]
	prx = random.choice(proxy)
	cookie = f"__dcfduid={randstr(32)}; __sdcfduid={randstr(96)}; locale=ru; __cf_bm={randstr(189)}"
	proxies = {'http': 'http://' + prx, 'https': 'http://' + prx}
	os, browser, user_agent, browserver, osvers = getInfo()
	xsuperprop = base64.b64encode(json.dumps(getSuperProp(os, browser, user_agent, browserver, osvers, 36127), separators=",:").encode()).decode()

	headers = {
		'Host': 'discord.com',
		'Connection': 'keep-alive',
		'X-Fingerprint': '',
		'User-Agent': user_agent,
		'X-Track': xsuperprop,
		'Accept': '*/*',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://discord.com/',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie': cookie,
		'dnt': '1',
		'sec-gpc': '1'
	}

	fingerprint_json = requests.get("https://discord.com/api/v9/experiments", headers=headers, proxies=proxies).text
	fingerprint = json.loads(fingerprint_json)["fingerprint"]

	solver = hCaptchaProxyless()
	solver.set_verbose(0)
	solver.set_key(key)
	solver.set_website_url("https://discord.com/api/v9/invites/" + invite)
	solver.set_website_key("4c672d35-0701-42b2-88c3-78380b0db560")
	g_response = solver.solve_and_return_solution()

	pld = '{"captcha_key":""}'
	a1 = len(pld) + len(str(g_response))

	headers = {
		'authority': 'discord.com',
		'method': 'POST',
		'path': '/api/v9/invites/' + invite,
		'scheme': 'https',
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': token,
		'content-length': str(a1),
		'content-type': 'application/json',
		'cookie': cookie,
		'origin': 'https://discord.com',
		'referer': 'https://discord.com/channels/@me',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': user_agent,
		'x-context-properties': xsuperprop,
		'x-debug-options': 'bugReporterEnabled',
		'x-discord-locale': 'ru',
		'x-fingerprint': fingerprint,
		'x-kl-ajax-request': 'Ajax_Request',
		'x-super-properties': xsuperprop
	}

	payload = {"captcha_key": str(g_response)}

	r = requests.post(f"https://discord.com/api/v9/invites/{invite}", json=payload, headers=headers, proxies=proxies)

	if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
		print(Fore.GREEN + f'SUCCESS {r.status_code}' + Fore.WHITE + ' | ' + Fore.YELLOW + Style.BRIGHT + token)
		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW(f'SUCCESS {r.status_code}' + ' | ' + token)

		now = datetime.now()
		tm = str(now.strftime('%Y-%m-%d'))

		with open(f"log/log_join({tm}).txt", "a", encoding="utf-8") as file:
			file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'Entered' + '      |  ' + 'Invite:' + invite + '  |  ' + 'Token: ' + token + '\n')

	else:
		print(Fore.RED + f'FAILED {r.status_code}' + Fore.WHITE + ' | ' + Fore.YELLOW + Style.BRIGHT + token)

		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW(f'FAILED {r.status_code}' + ' | ' + token)

		now = datetime.now()
		tm = str(now.strftime('%Y-%m-%d'))

		with open(f"log/log_join({tm}).txt", "a", encoding="utf-8") as file:
			file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'Entry error' + '  |  ' + 'Invite:' + invite + '  |  ' + 'Token: ' + token + '\n')

def leave1(token, gid):
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	user_agent = ''
	username = ''
	password = ''
	email = ''
	proxy = []

	with open(f"files/proxies.txt", "r", encoding="utf-8") as file:
		for line in file:
			proxy.append(line)

	proxy = [line.rstrip() for line in proxy]
	prx = random.choice(proxy)
	cookie = f"__dcfduid={randstr(32)}; __sdcfduid={randstr(96)}; locale=ru; __cf_bm={randstr(189)}"
	proxies = {'http': 'http://' + prx, 'https': 'http://' + prx}
	os, browser, user_agent, browserver, osvers = getInfo()
	xsuperprop = base64.b64encode(json.dumps(getSuperProp(os, browser, user_agent, browserver, osvers, 36127), separators=",:").encode()).decode()
	
	headers = {
		"authority": "discord.com",
		"method": "DELETE",
		"path": "/api/v9/users/@me/guilds/" + gid,
		"scheme": "https",
		"accept": "*/*",
		"accept-encoding": "gzip, deflate",
		"accept-language": "en-US",
		"authorization": token,
		"content-length": "17",
		"cookie": cookie,
		"origin": "https://discord.com",
		'referer': 'https://discord.com/channels/@me',
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"user-agent": user_agent,
		"x-context-properties": xsuperprop,
		"x-debug-options": "bugReporterEnabled",
		"x-super-properties": xsuperprop
	}

	payload = {
		"lurking":False
	}

	r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{gid}", json = payload, headers = header)

	now = datetime.now()

	if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
		print(Fore.GREEN + f'SUCCESS {r.status_code}' + Fore.WHITE + ' | ' + Fore.YELLOW + Style.BRIGHT + token)
		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW(f'SUCCESS {r.status_code}' + ' | ' + token)

		now = datetime.now()
		tm = str(now.strftime('%Y-%m-%d'))

		with open(f"log/log_leave({tm}).txt", "a", encoding="utf-8") as file:
			file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'Exited' + '       |  ' + 'Server id:' + gid + '  |  ' + 'Token: ' + token + '\n')

	else:
		print(Fore.RED + f'FAILED {r.status_code}' + Fore.WHITE + ' | ' + Fore.YELLOW + Style.BRIGHT + token)

		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW(f'FAILED {r.status_code}' + ' | ' + token)

		with open(f"log/log_leave({tm}).txt", "a", encoding="utf-8") as file:
			file.write("{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + '  |  ' + f'Exit error' + '   |  ' + 'Server id:' + gid + '  |  ' + 'Token: ' + token + '\n')