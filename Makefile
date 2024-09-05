VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
TEST=pytest
LINT=flake8
SRC=src/

# Create a virtual environment
$(VENV):
	python3 -m venv $(VENV)

# Install dependencies
install: $(VENV)
	$(PIP) install -r requirements.txt
	@echo "======================================"
	@echo "Run 'source $(VENV)/bin/activate' to activate the virtual environment."
	@echo "======================================"

# Run tests
test: $(VENV)
	$(PYTHON) -m $(TEST)

# Lint the code
lint: $(VENV)
	$(PYTHON) -m $(LINT) $(SRC)

# Clean up temporary files
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# Remove the virtual environment
clean-venv:
	rm -rf $(VENV)

# Rebuild everything (clean, remove venv, install deps, and run tests)
rebuild: clean clean-venv install test

# Default target when running "make" with no arguments
all: install test lint
