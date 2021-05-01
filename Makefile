.PHONY: list clean exe exe2 mypy

list:
	cat Makefile

clean:
	rm -fr ./dist

exe: clean
	pyinstaller --onefile convert.py

exe2: clean
	pyinstaller --onefile --noupx convert.py

mypy:
	mypy --config-file mypy.ini .
