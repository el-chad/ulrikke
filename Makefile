.PHONY: dev dev-ssl create-dataset

DATASET ?= prompt_interpreter_dataset

create-dataset:
	python3 -m clients.datasets.$(DATASET)

dev:
	uvicorn main:app --host 127.0.0.1 --port 8000 --reload

dev-ssl:
	uvicorn main:app --host 127.0.0.1 --port 9000 --reload \
		--ssl-keyfile=certs/localhost+2-key.pem \
		--ssl-certfile=certs/localhost+2.pem
