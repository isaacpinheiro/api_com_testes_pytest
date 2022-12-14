.PHONY: clean test

clean:
	rm -r __pycache__
	rm -r src/__pycache__
	rm -r src/config/__pycache__
	rm -r src/model/__pycache__
	rm -r src/controller/__pycache__

clean-test:
	make clean
	rm -r test/__pycache__
	rm -r test/config/__pycache__

test:
	pytest test/

run:
	flask run

run-test:
	python -m test.app-test

