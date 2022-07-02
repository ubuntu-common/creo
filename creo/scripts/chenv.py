#!/usr/bin/env python3

import argparse
import time
import os

from chenv.mount import mount, umount2, MNT_DETACH

def join_verify_path(root: str, path: dir) -> str:
	ret = os.path.join(root, path)
	if not os.path.exists(ret):
		raise OSError(f'Directory \'{ret}\' not found')
	return ret

def main(argparser: argparse.ArgumentParser, args: argparse.Namespace):
	if not os.path.exists(args.directory):
		argparser.error(f'Specified directory \'{args.directory}\' not found')

	try:
		mount('none', join_verify_path(args.directory, 'proc'), 'proc')
		mount('none', join_verify_path(args.directory, 'sys'), 'sysfs')
		mount('none', join_verify_path(args.directory, 'dev/pts'), 'devpts')
	except OSError as e:
		argparser.error(e.strerror)

	os.chroot(args.directory)
	os.chdir('/')
	os.system(args.command)

	try:
		umount2('/proc', MNT_DETACH)
		umount2('/sys', MNT_DETACH)
		umount2('/dev/pts', MNT_DETACH)
	except OSError as e:
		argparser.error(e.strerror)

if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-d', '--directory', required=True, help="path to root directory")
	argparser.add_argument('-c', '--command', required=True, help="command that will be execute in new environment")
	main(argparser, argparser.parse_args())
	argparser.exit(0)
