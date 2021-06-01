#!/usr/bin/python3
import sys
import re

import xml.etree.ElementTree as ET
import datetime

for line in sys.stdin:
    line = line.strip()
    if line[:4] != '<row':
        continue
    root = ET.fromstring(line)
    if 'Tags' not in root.attrib.keys() or 'CreationDate' not in root.attrib.keys():
        continue
    year = datetime.datetime.strptime(root.attrib['CreationDate'], '%Y-%m-%dT%H:%M:%S.%f').year
    tags = re.sub('[<>]', ' ', root.attrib['Tags']).split()
    for tag in tags:
        sys.stdout.write(f'{year}\t1\t{tag}\n')

