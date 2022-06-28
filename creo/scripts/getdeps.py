#!/usr/bin/env python3

from logging import warning

import argparse
import os

from getdeps.manifest import ManifestContext
from getdeps.platform import get_linux_type
from getdeps.handler import ArgumentHandler, HDLR_OK
from getdeps.installer import Installer

"""
	This directory is relative to the working directory!
"""
MANIFESTS_DIRECTORY = "manifests"

"""
	Be careful, the $id$ key will be replaced with your distribution ID during the parsing process!
"""
ALLOWED_SECTIONS = [
	'apt',
	'pacman'
]

"""
	Will be removed when the installer search system is integrated
"""
LINUX_INSTALLER_ASSOC = {
	'arch': [ 'pacman', [ '-S', '--noconfirm' ] ],
	'ubuntu': [ 'apt', [ 'install', '-y' ] ]
}

class ListHandler(ArgumentHandler):
	def handle(self, args: argparse.Namespace, manifests: list[ManifestContext]):
		for manifest in manifests:
			print(manifest.name())
		return HDLR_OK

class InstallHandler(ArgumentHandler):
	def handle(self, args: argparse.Namespace, manifests: list[ManifestContext]):
		type = get_linux_type()
		installer = Installer(LINUX_INSTALLER_ASSOC[type][0], LINUX_INSTALLER_ASSOC[type][1])
		allowed = [ section for section in ALLOWED_SECTIONS ]
		for manifest in manifests:
			for section in manifest.sections():
				if section not in allowed:
					warning('Cannot handle \'%s\' section in \'%s\' manifest. Not allowed', section, manifest.name())
					continue
				if section != installer.backend():
					continue
				installer.install(manifest)
		return HDLR_OK

def main(argparser: argparse.ArgumentParser) -> int:
	args = argparser.parse_args()
	manifests: list[ManifestContext] = []
	for elem in os.listdir(MANIFESTS_DIRECTORY):
		try:
			with open(f'./{MANIFESTS_DIRECTORY}/{elem}', 'r') as wrapper:
				manifests.append(ManifestContext(wrapper, elem))
		except EnvironmentError:
			warning('Cannot open file \'%s\' for reading', elem)
			return 1

	if args.list:
		ListHandler(argparser, args, manifests)

	if args.install:
		InstallHandler(argparser, args, manifests)

	return 0

if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-l', '--list', default=False, action="store_true", help="list all available manifests")
	argparser.add_argument('-i', '--install', default=False, action="store_true", help="install all available dependencies for system")
	argparser.exit(main(argparser))
