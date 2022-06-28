export TOPDIR:=${CURDIR}

include $(TOPDIR)/rules.mk

KCONFIG_MCONF:=kconfig-mconf

menuconfig: $(TOPDIR)/Config.in
	$(KCONFIG_MCONF) $^

include $(TOPDIR)/package/Makefile
