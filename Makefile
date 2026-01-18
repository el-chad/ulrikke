.PHONY: dev dev-ssl

dev:
	uvicorn main:app --host 127.0.0.1 --port 8000 --reload

dev-ssl:
	uvicorn main:app --host 127.0.0.1 --port 9000 --reload \
		--ssl-keyfile=certs/localhost+2-key.pem \
		--ssl-certfile=certs/localhost+2.pem
