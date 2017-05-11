#!/usr/bin/env python2.7

# example
# An example to search indicators based on given query
# Works on Demisto 2.5 onwards
#
# Author:       Slavik Markovich
# Version:      1.0
#

import json
import argparse
import csv
from datetime import datetime, timedelta
import demisto

def p(what):
    if verbose:
        print(what)

def options_handler():
    parser = argparse.ArgumentParser(description='Integrations and commands')
    parser.add_argument('-k', '--key', help='The API key to access the server', required=True)
    parser.add_argument('-s', '--server', help='The server URL to connect to', required=True)
    parser.add_argument('-q', '--quiet', action='store_false', dest='verbose', default=True, help="no extra prints")
    parser.add_argument('-o', '--output', help='The output CSV file', default='indicators.csv')
    parser.add_argument('-f', '--filter', help='The filter to use when searching indicators')
    parser.add_argument('-d', '--delta', help='The delta period we should search for - acceptible values are 1d, 5h, 30m, etc.', default='7d')
    options = parser.parse_args()
    global verbose
    verbose = options.verbose
    return options

def fromDate(delta):
    fromD = datetime.now()
    d = int(delta[:-1])
    t = delta[-1:]
    if t == 'm':
        fromD = fromD - timedelta(minutes=d)
    elif t == 'h':
        fromD = fromD - timedelta(hours=d)
    elif t == 'd':
        fromD = fromD - timedelta(days=d)
    else:
        fromD = fromD - timedelta(days=7)
    return fromD.strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    options = options_handler()
    c = demisto.DemistoClient(options.key, options.server)
    postData = {'sort': [{'field': 'value', 'asc': True}]}
    if options.filter:
        postData['query'] = options.filter
    if options.delta:
        postData['fromDate'] = fromDate(options.delta)
    indicatorsResponse = c.req('POST', 'indicators/search', postData)
    if indicatorsResponse.status_code != 200:
        raise RuntimeError('Error getting indicators data - %d (%s)' % (indicatorsResponse.status_code, indicatorsResponse.reason))
    indicators = indicatorsResponse.json()
    with open(options.output, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Value', 'Type', 'Source', 'FirstSeen', 'LastSeen', 'Score'])
        writer.writeheader()
        for i in indicators['iocObjects']:
            writer.writerow({'Value': i['value'], 'Type': i['indicator_type'], 'Source': i['source'], 'FirstSeen': i['firstSeen'], 'LastSeen': i['lastSeen'], 'Score': i['score']})

if __name__ == '__main__':
    main()