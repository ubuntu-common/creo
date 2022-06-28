import io
import configparser

class ManifestReader:
	def __init__(self, manifest: io.TextIOWrapper) -> None:
		self.__parser = configparser.ConfigParser(allow_no_value=True)
		self.__parser.read_file(manifest)

	def sections(self) -> list[str]:
		return self.__parser.sections()

	def get(self, section: str) -> list[str]:
		return list(self.__parser[section])

class ManifestContext(ManifestReader):
	def __init__(self, manifest: io.TextIOWrapper, name: str) -> None:
		ManifestReader.__init__(self, manifest)
		self.__name = name

	def name(self) -> str:
		return self.__name
