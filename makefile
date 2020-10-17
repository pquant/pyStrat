ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

VENV := $(ROOT_DIR)/venv

venv:
	$(ROOT_DIR)/create-venv.sh

.PHONY: venv
