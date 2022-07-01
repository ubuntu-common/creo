import os
import subprocess

from getdeps.manifest import ManifestContext

BACKEND_RULES = {
	'arch': {
		'pacman': [ '-S', '--noconfirm' ],
		'yay': [ '-S', '--noconfirm' ],
		'paru': [ '-S', '--noconfirm' ],
		'pikaur': [ '-S', '--noconfirm' ],
		'trizen': [ '-S', '--noconfirm' ],
		'aura': [ '-S', '--noconfirm' ],
		'pamac': [ 'install', '--no-confirm' '--aur' ]
	},
	'ubuntu': { 'apt': [ 'install', '-y' ] }
}

def get_supported_backends(system_id: str) -> list[str]:
	return list(BACKEND_RULES[system_id])

def get_avaliable_backends(system_id: str) -> list[str]:
	avaliable: list[str] = [ ]
	supported = get_supported_backends(system_id)
	for path in os.environ['PATH'].split(':'):
		for backend in supported:
			path_backend = f'{path}/{backend}'
			if os.path.isfile(path_backend) is False:
				continue
			if os.access(path_backend, os.X_OK) is False:
				raise RuntimeError(f'Supported \'{path_backend}\' backend found, but it\'s can\'t be executed. No executable access rights')
			avaliable.append(backend)
	return avaliable

class Installer:
	def __init__(self, system_id: str):
		self.__system_id = system_id
		self.__avaliable_backends = get_avaliable_backends(system_id)

	def system_id(self) -> str:
		return self.__system_id

	def install(self, manifests: list[ManifestContext], backend: str = None):
		avaliable: list[str] = [ ]
		targets: dict[str, list[str]] = { }
		if backend:
			if backend not in self.__avaliable_backends:
				raise RuntimeError(f'Specified backend \'{backend}\' is unsupported')
			avaliable = [ backend ]
		else:
			avaliable = self.__avaliable_backends
		for manifest in manifests:
			for section in manifest.sections():
				try:
					section_id, section_backend = section.split('-')
				except ValueError:
					raise RuntimeError(f'Cannot handle manifest \'{manifest.name()}\'. Unexpected section \'{section}\'')
				if section_id != self.__system_id:
					continue
				if section_backend not in avaliable:
					continue
				if section_backend not in targets:
					targets[section_backend] = []
				targets[section_backend] += manifest.get(section)
		for target in targets:
			args = BACKEND_RULES[self.__system_id][target]
			subprocess.run([ target ] + args + targets[target])
