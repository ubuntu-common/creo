include $(INCLUDE_DIR)/foreach.mk

curdir:=package

$(curdir)/prepare: $(curdir)/*/Makefile
	$(call Foreach/Makefile,$^,prepare)

$(curdir)/install: $(curdir)/*/Makefile
	$(call Foreach/Makefile,$^,install)

$(curdir)/cleanup: $(curdir)/*/Makefile
	$(call Foreach/Makefile,$^,cleanup)
