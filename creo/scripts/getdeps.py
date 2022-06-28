#!/usr/bin/env python3

from logging import warning

import argparse
import os

from getdeps.manifest import ManifestContext
from getdeps.platform import get_linux_type
from getdeps.handler import ArgumentHandler, HDLR_OK, HDLR_ERR
from getdeps.installer import Installer

"""
	This directory is relative to the working directory!
"""
MANIFESTS_DIRECTORY = "manifests"

class ListHandler(ArgumentHandler):
	def handle(self, args: argparse.Namespace, manifests: list[ManifestContext]):
		print('\n'.join([ manifest.name() for manifest in manifests ]))
		return HDLR_OK

class InstallHandler(ArgumentHandler):
	def handle(self, args: argparse.Namespace, manifests: list[ManifestContext]):
		installer = Installer(get_linux_type())
		installer.install(manifests, args.backend)
		return HDLR_OK

def main(argparser: argparse.ArgumentParser) -> int:
	manifests: list[ManifestContext] = [ ]
	for elem in os.listdir(MANIFESTS_DIRECTORY):
		try:
			with open(f'./{MANIFESTS_DIRECTORY}/{elem}', 'r') as wrapper:
				manifests.append(ManifestContext(wrapper, elem))
		except EnvironmentError:
			warning('Cannot open file \'%s\' for reading', elem)
			return HDLR_ERR

	args = argparser.parse_args()

	if args.list:
		ListHandler(argparser, args, manifests)

	if args.install:
		InstallHandler(argparser, args, manifests)

	return HDLR_OK

if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-l', '--list', default=False, action="store_true", help="list all available manifests")
	argparser.add_argument('-i', '--install', default=False, action="store_true", help="install all available dependencies for system")
	argparser.add_argument('-b', '--backend', help="backend that will be used for installation")
	argparser.exit(main(argparser))
