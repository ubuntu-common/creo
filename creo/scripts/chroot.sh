#!/bin/bash

# Here we need to implement the simplest CLI utility based on the GNU convention.

[[ -n "$1" ]] || {
	echo "Usage: $0 DIRECTORY"
	exit 1
}

mount none -t proc $1/proc
mount none -t sysfs $1/sys
mount none -t devpts $1/dev/pts
chroot $1
umount -R $1/proc
umount -R $1/sys
umount -R $1/dev/pts
