.PHONY: db clean

db: mycampus.sqlite3 starbucks.sqlite3

mycampus.sqlite3:
	cp ../datasets/2017-01-10.sqlite3.gz ./mycampus.sqlite3.gz
	gunzip mycampus.sqlite3.gz

starbucks.sqlite3:
	cp ../datasets/starbucks.sqlite3.gz ./starbucks.sqlite3.gz
	gunzip starbucks.sqlite3.gz

clean:
	rm mycampus.sqlite3 starbucks.sqlite3
