#!/usr/bin/python

# get stock data

import urllib2
import json

#"^STOXX50E","^DJI","^GSPC"
stocklist={"INDEXDB%3ADAX","INDEXDJX%3A.DJI","INDEXSP%3A.INX"}

query = ""
for i in stocklist:
    query = i + "," + query

url = "https://finance.google.com/finance/info?client=ig&q=" + query
try:
    u = urllib2.urlopen(url)
    query = u.read()
    obj = json.loads(query[4:-1])
    for ticker in obj:
        print "{} {} {} | color=".format(ticker["t"], ticker["l"], ticker["c"]), "red" if float(ticker["c"]) < 0 else "green"
except Exception as ex:
    print "offline"
