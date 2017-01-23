build:
	mkdir -p ./build
	gunzip --stdout < ../datasets/Oshawa_Streets.csv.gz > ./build/data.csv

run:
	python load_sqlite.py build/data.csv

plot:
	python plot.py

clean:
	rm -rf ./build
