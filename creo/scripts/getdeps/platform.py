import csv

def get_linux_type() -> str:
	with open('/etc/os-release', 'r') as wrapper:
		data = dict(csv.reader(wrapper, delimiter="="))
	return data['ID']