import ctypes
import ctypes.util
import os

MNT_DETACH = 2

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)
def mount(source: str, target: str, fs: str = '', options: str = ''):
	ret = libc.mount(source.encode(), target.encode(), fs.encode(), 0, options.encode())
	if ret != 0:
		errno = ctypes.get_errno()
		raise OSError(errno, f'Error mounting {source} ({fs}) on {target} with options \'{options}\': {os.strerror(errno)}')

libc.umount2.argtypes = (ctypes.c_char_p, ctypes.c_int)
def umount2(target: str, flags: int):
	ret = libc.umount2(target.encode(), flags)
	if ret != 0:
		errno = ctypes.get_errno()
		raise OSError(errno, f'Error unmounting {target}: {os.strerror(errno)}')
