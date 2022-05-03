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
import discum
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


def parse(token, serv, chan):
	bot = discum.Client(token=token)


	def close_after_fetching(resp, guild_id):
		if bot.gateway.finishedMemberFetching(guild_id):
			lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
			bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
			bot.gateway.close()


	def get_members(guild_id, channel_id):
		bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
		bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.run()
		bot.gateway.resetSession()
		return bot.gateway.session.guild(guild_id).members
		if platform == 'win32':
			os.system("cls")
		else:
			os.system("clear")

	memberslist = []
	now = datetime.now()
	members = get_members(serv, chan)

	for memberID in members:
		memberslist.append(memberID)
		print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + Fore.WHITE + ' | ' + Fore.GREEN + f'PARSED' + Fore.WHITE + ' | ' + Fore.YELLOW + Style.BRIGHT + memberID + '\n')
		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW(now.strftime('%Y-%m-%d / %H:%M:%S') + ' | ' +  f'PARSED' + ' | ' + memberID)
		else:
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + Fore.WHITE + ' | ' + Fore.RED + f'FAILED' + Fore.WHITE + ' | ' + Fore.YELLOW + Style.BRIGHT + memberID + '\n')
		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW(now.strftime('%Y-%m-%d / %H:%M:%S') + ' | ' +  f'FAILED' + ' | ' + memberID)

	f = open('files/users.txt', "a")
	for element in memberslist:
		f.write(element + '\n')
	f.close()