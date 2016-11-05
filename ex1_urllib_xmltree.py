#!/usr/bin/python3

import urllib.request as ur
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: ex1_urllib_xmltree.py route stopid')

print('Command Options : ', sys.argv)
route = sys.argv[1]
stopid = sys.argv[2]


from xml.etree.ElementTree import XML

#u = ur.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14788&route=22')
u = ur.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(route,stopid))
print(u)
data = u.read()
print(data)

doc = XML(data)
print(doc)

for pt in doc.findall('.//pt'):
    print(pt.text)
