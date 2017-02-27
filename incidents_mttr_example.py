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
    parser.add_argument('-g', '--group', help='The field to group by to calculate mttr, default is owner', default='owner')
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
        field = ''
        if options.group == 'owner':
            field = i['owner'] if i['owner'] else 'dbot'
        else:
            field = i[options.group]
        if field in mttr:
            mttr[field]['mttr'] = mttr[field]['mttr'] + d.total_seconds()
            mttr[field]['incidents'] = mttr[field]['incidents'] + 1
        else:
            mttr[field] = {'mttr': d.total_seconds(), 'incidents': 1}
    with open(options.output, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Field', 'Incidents', 'MTTR'])
        writer.writeheader()
        for f in mttr:
            writer.writerow({'Field': f, 'Incidents': mttr[f]['incidents'], 'MTTR': int(mttr[f]['mttr'] / mttr[f]['incidents'] / 60)})

if __name__ == '__main__':
    main()