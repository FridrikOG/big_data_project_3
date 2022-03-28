# Foobar

This is a readme for project 3 in the class T-764-DATA

## Installation

---
```
  Install Python (you do not need conda for this)
```
```
  source venv/bin/activate (inside the main directory)
```
```  
  Pip install pipenv
```
```
pip install -r requirements.txt
```

## The scraper

Looks at this link: https://www.mbl.is/200milur/afurdir/ gets the name, price, and last date transacted
for seafood in Iceland. It then cleans the data, then it checks mongoDB if it already has the same record
in the database by comparing the dates and inserts it if not.

## InfluxDB

The time series data is uploaded through the localhost UI that is offered by InfluxDB or through the code. The formatted data is in convertcsv.csv under data and an older influxdb file is also in data. This code does not do much of anything, point was just to understand better how influxDB handles data and perform queries.

## License

[MIT](https://choosealicense.com/licenses/mit/)
