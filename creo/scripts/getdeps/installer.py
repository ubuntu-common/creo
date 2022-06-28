import subprocess

from getdeps.manifest import ManifestContext

"""
	Will be changed soon
"""
class Installer():
	def __init__(self, backend: str, arguments: list[str]) -> None:
		self.__backend = backend
		self.__arguments = arguments

	def backend(self) -> str:
		return self.__backend

	def install(self, manifest: ManifestContext) -> int:
		targets = manifest.get(self.__backend)
		completed = subprocess.run([ self.__backend ] + self.__arguments + targets)
		return completed.returncode
