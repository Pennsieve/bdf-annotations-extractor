.PHONY: help test run

SERVICE_NAME  ?= "bdf-annotation-extractor"

.DEFAULT: help

help:
	@echo "Make Help for $(SERVICE_NAME)"
	@echo ""
	@echo "make run				- run the extractor locally via docker-compose"

run:
	docker-compose -f docker-compose.yml down --remove-orphans
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up --exit-code-from extractor

run-interactive:
	docker-compose -f docker-compose.yml run extractor