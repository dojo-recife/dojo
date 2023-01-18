SHELL = /bin/bash -l

DIR_NAME = dojo

python_setup:
	mkdir ${DIR_NAME} && touch ${DIR_NAME}/test.py ${DIR_NAME}/main.py && 
	cp setup_tests/setup_python.py ${DIR_NAME}/test.py