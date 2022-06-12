all: prereq download install

download:
ifeq ($(wildcard $(CACHE_DIR)),)
	@mkdir -p $(CACHE_DIR)
	@debootstrap \
		--arch=$(ARCH) \
		--variant=$(VARIANT) \
		--download-only \
		$(SUITE) \
		$(CACHE_DIR) \
		http://us.archive.ubuntu.com/ubuntu/
endif

prereq:
ifneq ($(shell id -u),0)
	@echo "You cannot perform this action within non root user!"
	@exit 1
endif

install: prereq download
	@mkdir -p $(CHROOT_DIR)
	@cp -r $(CACHE_DIR)/* $(CHROOT_DIR)
	@debootstrap \
		--arch=$(ARCH) \
		--variant=$(VARIANT) \
		$(SUITE) \
		$(CHROOT_DIR) \
		http://us.archive.ubuntu.com/ubuntu/
	install -m 754 -d $(CHROOT_DIR)/hooks
	install -m 754 -D $(HOOKS_DIR)/chroot/* $(CHROOT_DIR)/hooks

chroot: prereq
	@mount none -t proc $(CHROOT_DIR)/proc
	@mount none -t sysfs $(CHROOT_DIR)/sys
	@mount none -t devpts $(CHROOT_DIR)/dev/pts
	@chroot $(CHROOT_DIR)
	@umount -R $(CHROOT_DIR)/proc
	@umount -R $(CHROOT_DIR)/sys
	@umount -R $(CHROOT_DIR)/dev/pts

clean: prereq
	@rm -rf $(CACHE_DIR) $(CHROOT_DIR)

.PHONY: all download prereq install clean
