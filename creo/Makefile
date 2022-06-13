export TOPDIR:=${CURDIR}

include $(TOPDIR)/rules.mk

# We really have a problem with this tool!
# Lookup the scripts/manifests/kconfig-frontends comment!
KCONFIG_MCONF:=kconfig-mconf

menuconfig: $(TOPDIR)/Config.in
	$(KCONFIG_MCONF) $^

include $(TOPDIR)/package/Makefile
