SHELL := /bin/sh

doc:
	snowboard html -o docs/chjunstossomosmais.html docs/chjunstossomosmais.apib
	vanadia --input docs/chjunstossomosmais.apib --output docs/chjunstossomosmais.postman_collection.json

clean:
	@rm -f .coverage 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete

format:
	@black . 

sort:
	@isort

lint:
	@flake8 junstossomosmais

test: clean lint
	@black --check junstossomosmais
	@isort -c
	python -m pytest --cov=core
	#./wait-for-it.sh db:5432 -s -t 120 -- python -m pytest --cov=junstossomosmais --cov=feira

dump_data:
	python manage.py load_data -f DEINFO_AB_FEIRASLIVRES_2014.csv