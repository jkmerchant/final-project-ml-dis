
help:
	cat Makefile
run:
	docker-compose up
exec:
	docker-compose exec final-project-ml-dis bash
build: stop .FORCE
	docker-compose build
rebuild: stop .FORCE
	docker-compose build --no-cache
stop:
	docker stop final-project-ml-dis || true; docker rm final-project-ml-dis || true;
.FORCE:
