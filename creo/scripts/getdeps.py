#!/usr/bin/env python3

import os
import sys
import csv
import configparser

def parse_config(file) -> dict:
	with open(file) as desc:
		reader = csv.reader(desc, delimiter="=")
		return dict(reader)

def get_installer(id) -> int:
	"""Only Ubuntu and Arch Linux support right now!"""
	if id == 'arch':
		return 'pacman -S --noconfirm'
	elif id == 'ubuntu':
		return 'apt install -y'

class ManifestInstaller:
	def __init__(self, manifests_dir = None) -> None:
		self.__os_id = parse_config('/etc/os-release')['ID']
		self.__installer = get_installer(self.__os_id)
		self.__parser = configparser.ConfigParser(allow_no_value=True)
		if manifests_dir:
			for mfst in os.listdir(manifests_dir):
				self.add_manifest(os.path.join(manifests_dir, mfst))

	def add_manifest(self, file) -> None:
		self.__parser.read(file)
		for pkg in self.__parser[self.__os_id]:
			self.__installer += f' {pkg}'
		self.__parser.clear()

	def install(self) -> int:
		return os.system(self.__installer)

if __name__ == "__main__":
	installer = ManifestInstaller(os.path.join(os.path.dirname(__file__), 'manifests'))
	sys.exit(installer.install())
