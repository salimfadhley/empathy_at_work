import csv
from urllib.request import geturl

CSV_SOURCE = r"https://docs.google.com/spreadsheets/d/1AKn-uP0FE8NpqWt8zbFedIQIsYJq6fPIleCEtMAGH1c/pub?gid=558503423&single=true&output=csv"

def fetcher(url=CSV_SOURCE):
    document = geturl(url)
    reader = csv.DictReader(document)
    for row in reader:
        yield row

