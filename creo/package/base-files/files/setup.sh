#!/bin/sh

HOOKS_DIR=/etc/creo/hooks

if test -d "$HOOKS_DIR"; then
	for hook in "$HOOKS_DIR/*"; do
		test -rx "$hook" && . "$hook"
	done
fi
