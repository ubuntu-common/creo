import argparse
import errno
import abc
import sys

from getdeps.manifest import ManifestContext

HDLR_OK = 0
HDLR_ERR = 1

class ArgumentHandler(metaclass=abc.ABCMeta):
	def __init__(self, argparser: argparse.ArgumentParser, args: argparse.Namespace, manifests: list[ManifestContext]):
		ret = self.handle(args, manifests)
		if ret == HDLR_OK:
			return
		if ret == HDLR_ERR:
			argparser.print_help()
		sys.exit(ret)

	@abc.abstractmethod
	def handle(self, args: argparse.Namespace, manifests: list[ManifestContext]) -> int:
		raise NotImplementedError
