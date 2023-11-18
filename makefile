# Variáveis
PYTHON = python
PIP = pipenv
FLASK_APP = run.py
FLASK_ENV = development

help:
	################################################################
	############										############
	############	COMANDOS MAKE DA APLICAÇÃO			############
	############										############
	################################################################
	@echo
	# Todos os comandos são executados com o $ make <comando>
	@echo
	# Lista de comandos:
	@echo run: 			Executa o servidor Flask
	@echo test: 		Roda os testes
	@echo db-up:	 	Subir o banco
	@echo db-down: 	Baixar o banco

run:
	FLASK_APP=$(FLASK_APP) FLASK_ENV=$(FLASK_ENV) $(PYTHON) -m flask run

test:
	pytest

db-up:
	docker-compose up -d

db-down:
	docker-compose down
