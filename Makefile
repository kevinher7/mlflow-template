.PHONY: lint format typecheck test all

lint:
	ruff check src/ --fix

format:
	ruff format src/

typecheck:
	ty check src/

test:
	pytest

all: lint format typecheck test
