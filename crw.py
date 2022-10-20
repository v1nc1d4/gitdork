import requests
from bs4 import BeautifulSoup
import argparse
import sys
import os

class Crawler:
	def __init__(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("-u", "--url", dest="url", help="Target url.")
		args = parser.parse_args()
		if not args.url:
			sys.exit(parser.print_help())
		else:
			self.url = args.url
	def crw(self):
		cont = requests.get(self.url).content
		soup = BeautifulSoup(cont, 'html.parser')
		for link in soup.find_all('a'):
			print (link.get('href'))

if __name__ == '__main__':
	cls = Crawler()
	cls.crw()
