PACKAGE_NAME := greentea
BASE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
PYTHON_VERSION := 3.8.0
PYENV_FILE := $(BASE_DIR).python-version
DOC_BUILD_DIR := $(BASE_DIR).doc_build
DOC_VENV := $(BASE_DIR).doc_venv
DOC_DIR := $(BASE_DIR)doc

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

doc: $(DOC_VENV)bin/sphinx-build $(DOC_BUILD_DIR)conf.py $(DOC_BUILD_DIR)index.rst ## Generate docs.
	sphinx-apidoc -M -f -o $(DOC_BUILD_DIR) $(PACKAGE_NAME) && \
	sphinx-build -a $(DOC_BUILD_DIR) $(DOC_DIR)

$(DOC_BUILD_DIR)conf.py:
	cd $(BASE_DIR) && \
	mkdir -p $(DOC_BUILD_DIR) && \
	cp config/conf.py $(DOC_BUILD_DIR)/conf.py

$(DOC_BUILD_DIR)index.rst:
	cd $(BASE_DIR) && \
	mkdir -p $(DOC_BUILD_DIR) && \
	cp config/index.py $(DOC_BUILD_DIR)/conf.py

$(DOC_VENV)bin/sphinx-build: $(PYENV_FILE)
	cd $(BASE_DIR) && \
	python -m venv $(DOC_VENV) && \
	pip install -e .[doc]

$(PYENV_FILE): 
	cd $(BASE_DIR) && \
	pyenv local $(PYTHON_VERSION)

.PHONY: help
