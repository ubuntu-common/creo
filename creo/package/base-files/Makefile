include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/package.mk
include $(CONFIG_FILE)

define Package/base-files
	DESCRIPTION:=Base filesystem for Ubuntu Common.
	AUTHOR:=beryll1um
endef

$(eval $(call Package/Setup,base-files))

define Package/base-files/prepare
	$(DEBOOTSTRAP) \
		--arch=$(CONFIG_ARCH) \
		--variant=$(CONFIG_VARIANT) \
		--download-only \
		$(CONFIG_SUITE) \
		$(TMP_DIR) \
		$(CONFIG_SOURCE)
endef

define Package/base-files/install
	$(CP) $(TMP_DIR)/* $(STAGING_DIR)
	$(DEBOOTSTRAP) \
		--arch=$(CONFIG_ARCH) \
		--variant=$(CONFIG_VARIANT) \
		$(CONFIG_SUITE) \
		$(STAGING_DIR) \
		$(CONFIG_SOURCE)
	$(INSTALL_DIR) $(STAGING_DIR)/etc/creo
	$(INSTALL_DIR) $(STAGING_DIR)/etc/creo/hooks
	$(INSTALL_BIN) ./files/hooks/* $(STAGING_DIR)/etc/creo/hooks
	$(INSTALL_BIN) ./files/setup.sh $(STAGING_DIR)/etc/creo
	$(CHENV) --directory=$(STAGING_DIR) --command=/etc/creo/setup.sh
endef

$(eval $(call Package/RegPrepare,base-files,prepare))
$(eval $(call Package/RegInstall,base-files,install))
$(eval $(call Package/RegCleanup,base-files))
