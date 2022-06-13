define Foreach/Makefile
	$(foreach elt,$1,$(MAKE) -C $(dir $(elt)) $2)
endef
