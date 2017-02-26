#!/usr/bin/env python2.7

# example
# An example to retrieve incident mttr statistics per analyst
#
# Author:       Slavik Markovich
# Version:      1.0
#

import json
import argparse
from datetime import date, datetime, timedelta
import csv
import demisto

def format_dt(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

def parse_dt(dt):
    return datetime.strptime(dt[:19], '%Y-%m-%dT%H:%M:%S')

def p(what):
    if verbose:
        print(what)

def options_handler():
    parser = argparse.ArgumentParser(description='Incident MTTR statistics for a time period')
    parser.add_argument('-u', '--user', help='The username for the login', required=True)
    parser.add_argument('-p', '--password', help='The password for the login', required=True)
    parser.add_argument('-s', '--server', help='The server URL to connect to', required=True)
    monthAgo = date.today() - timedelta(days=30)
    parser.add_argument('-f', '--filter', help='The filter query to chose the alerts, default is closed incidents in last month', default='status:=2 and closed:>%s' % format_dt(monthAgo))
    parser.add_argument('-q', '--quiet', action='store_false', dest='verbose', default=True, help="no extra prints")
    parser.add_argument('-o', '--output', help='The output CSV file', default='mttr.csv')
    options = parser.parse_args()
    global verbose
    verbose = options.verbose
    return options

def main():
    options = options_handler()
    c = demisto.DemistoClient(options.user, options.password, options.server)
    c.Login()
    p('using filter %s' %  options.filter)
    incidents = c.SearchIncidents(0, 10000, options.filter)
    p('Total #incidents: %d' % (incidents['total']))
    mttr = {}
    for i in incidents['data']:
        if not 'closed' in i or not i['closed']:
            continue
        created = parse_dt(i['created'])
        closed = parse_dt(i['closed'])
        d = closed - created
        owner = i['owner'] if i['owner'] else 'dbot'
        if owner in mttr:
            mttr[owner]['mttr'] = mttr[owner]['mttr'] + d.total_seconds()
            mttr[owner]['incidents'] = mttr[owner]['incidents'] + 1
        else:
            mttr[owner] = {'mttr': d.total_seconds(), 'incidents': 1}
    with open(options.output, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Analyst', 'Incidents', 'MTTR'])
        writer.writeheader()
        for analyst in mttr:
            writer.writerow({'Analyst': analyst, 'Incidents': mttr[analyst]['incidents'], 'MTTR': int(mttr[analyst]['mttr'] / mttr[analyst]['incidents'] / 60)})

if __name__ == '__main__':
    main()