run:
	python3 run_demo.py
test:
	python3 -m unittest discover -s tests -v
.PHONY: run test
