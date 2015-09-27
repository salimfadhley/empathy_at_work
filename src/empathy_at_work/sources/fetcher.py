import csv
from urllib.request import urlopen

CSV_SOURCE = r"https://docs.google.com/spreadsheets/d/1AKn-uP0FE8NpqWt8zbFedIQIsYJq6fPIleCEtMAGH1c/pub?gid=558503423&single=true&output=csv"

def loader(url):
    document = urlopen(url)
    for row in document:
        yield row.decode("utf-8")

def fetcher(url=CSV_SOURCE):
    reader = csv.DictReader(loader(url))
    for row in reader:
        yield row

