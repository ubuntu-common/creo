import csv

"""
	File that contains variables that is defined by the operating system vendor
"""
OS_RELEASE_PATH = '/etc/os-release'

def get_linux_type() -> str:
	with open(OS_RELEASE_PATH, 'r') as wrapper:
		data = dict(csv.reader(wrapper, delimiter="="))
	try:
		return data['ID']
	except KeyError:
		raise RuntimeError(f'File \'{OS_RELEASE_PATH}\' doesn\'t contains \'ID\' field')
