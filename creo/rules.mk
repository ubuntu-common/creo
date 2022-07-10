export STAGING_DIR:=$(TOPDIR)/staging_dir
export INCLUDE_DIR:=$(TOPDIR)/include
export SCRIPTS_DIR:=$(TOPDIR)/scripts
export CONFIG_FILE:=$(TOPDIR)/.config
export TMP_DIR:=$(TOPDIR)/tmp

PYTHON:=python3

MKDIR:=mkdir -p
CP:=cp -fpR
RM:=rm -rf

DEBOOTSTRAP:=debootstrap

INSTALL_BIN:=install -m755
INSTALL_DIR:=install -d -m755
INSTALL_DATA:=install -m0644

CHENV:=$(PYTHON) $(SCRIPTS_DIR)/chenv.py
