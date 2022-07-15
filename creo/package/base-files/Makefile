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
		--include=$(CONFIG_INCLUDE) \
		--download-only \
		$(CONFIG_SUITE) \
		$(TMP_DIR) \
		$(CONFIG_SOURCE)
endef

define Package/base-files/install
	$(CP) $(TMP_DIR)/* $(STAGING_DIR)
	$(INSTALL_DIR) $(STAGING_DIR)/etc
	$(INSTALL_DATA) ./files/etc/{hostname,hosts} $(STAGING_DIR)/etc
	$(DEBOOTSTRAP) \
		--arch=$(CONFIG_ARCH) \
		--variant=$(CONFIG_VARIANT) \
		--include=$(CONFIG_INCLUDE) \
		$(CONFIG_SUITE) \
		$(STAGING_DIR) \
		$(CONFIG_SOURCE)
endef

$(eval $(call Package/RegPrepare,base-files,prepare))
$(eval $(call Package/RegInstall,base-files,install))
$(eval $(call Package/RegCleanup,base-files))
