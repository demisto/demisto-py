#!/usr/bin/env python

#
# An example to search incidents based on a given query
#


import argparse
from datetime import datetime, timedelta
import demisto
import json


def options_handler():
    parser = argparse.ArgumentParser(description='Integrations and commands')
    parser.add_argument(
        'key', help='The API key to access the server')
    parser.add_argument(
        'server', help='The server URL to connect to')
    parser.add_argument(
        '-f', '--filter', help='The filter to use when searching indicators')
    parser.add_argument(
        '-d', '--delta', 
        help='The delta period we should search for - acceptible values are 1d, 5h, 30m, etc. Only used if filter option is not specified',
        default='7d')
    options = parser.parse_args()
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
    if not options.filter and options.delta:
        options.filter = 'created:>="{}"'.format(fromDate(options.delta))
    incidents = c.SearchIncidents(0, 100, options.filter)
    print(json.dumps(incidents, indent=2))


if __name__ == '__main__':
    main()
