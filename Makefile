cat:
	cat Makefile

run:
	uv run convert.py

mypy:
	uv run mypy --config-file mypy.ini .
