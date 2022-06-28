#!/bin/sh

HOOKS_DIR=/etc/creo/hooks

if [ -d "$HOOKS_DIR" ]; then
	for hook in "$HOOKS_DIR"/*; do
		if [ ! -r "$hook" ] || [ ! -x "$hook" ]; then
			echo "Cannot read or execute hook $hook"
			continue
		fi
		. $hook
	done
fi
