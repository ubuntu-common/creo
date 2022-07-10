include $(TOPDIR)/rules.mk

define Package/Setup
	NAME:=$1
	$(call Package/$1)
	TMP_DIR:=$(TMP_DIR)/$1
endef

define Package/RegValidate

ifneq ($2, )
ifneq ($3, )
ifneq ($2,$3)
	$$(error $0: Package/$1 try to register '$2' target under '$3' registration function)
endif
endif
	$(call Package/$1/$2)
endif
endef

define Package/RegPrepare
prepare:
	$(MKDIR) $(STAGING_DIR) $(TMP_DIR)
	$(call Package/RegValidate,$1,$2,prepare)
endef

define Package/RegInstall
install:
	$(call Package/RegValidate,$1,$2)
endef

define Package/RegCleanup
cleanup:
	$(call Package/RegValidate,$1,$2,cleanup)
	$(RM) $(STAGING_DIR)
endef

define Package/Forward
$(1)/prepare: $(1)/Makefile
	$(MAKE) -C $(1) prepare

$(1)/install: $(1)/Makefile
	$(MAKE) -C $(1) install

$(1)/cleanup: $(1)/Makefile
	$(MAKE) -C $(1) cleanup
endef
