#!/usr/bin/env python3

import argparse
import os

from getdeps.manifest import ManifestContext
from getdeps.platform import get_linux_type
from getdeps.installer import Installer

"""
	This directory is relative to the working directory!
"""
MANIFESTS_DIRECTORY = "manifests"

def main(argparser: argparse.ArgumentParser, args: argparse.Namespace):
	manifests: list[ManifestContext] = [ ]

	if not args.directory:
		args.directory = MANIFESTS_DIRECTORY

	if not os.path.exists(args.directory):
		argparser.error(f'Manifests directory doesn\'t exists')

	for elem in os.listdir(args.directory):
		try:
			with open(f'./{args.directory}/{elem}', 'r') as wrapper:
				manifests.append(ManifestContext(wrapper, elem))
		except EnvironmentError:
			argparser.error(f'Cannot open file \'{elem}\' for reading')

	if args.action == 'list':
		print('\n'.join([ manifest.name() for manifest in manifests ]))

	if args.action == 'install':
		try:
			installer = Installer(get_linux_type())
			installer.install(manifests, args.manager)
		except RuntimeError as e:
			argparser.error(e.args[0])

if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-a', '--action', required=True, choices=['list', 'install'], help="action that will be produced")
	argparser.add_argument('-m', '--manager', help="single package manager to be used for the action")
	argparser.add_argument('-d', '--directory', help="path to directory with manifests")
	main(argparser, argparser.parse_args())
	argparser.exit(0)
