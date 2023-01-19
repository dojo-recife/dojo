# O Makefile é um arquivo onde você consegue definir uma série de tarefas a serem 
# executadas pelo comando criado tendo o comando `make` como antecessor.
# Exemplos de tarefas que podem ser criadas no Makefile:
#   - Criação de diretórios, execução de comandos etc
SHELL = /bin/bash -l

DIR_NAME = dojo_recife

python_setup:
	mkdir ${DIR_NAME} && touch ${DIR_NAME}/test.py ${DIR_NAME}/main.py && 
	cp setup_tests/setup_python.py ${DIR_NAME}/test.py