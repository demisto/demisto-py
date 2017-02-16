#!/usr/bin/env python2.7

# example
# An example of helper utility to do stuff on multiple incidents based on filter
#
# Stuff can be closing incidents, running a command, changing type or changing playbook
#
# Author:       Slavik Markovich
# Version:      1.0
#

import json
import argparse
from datetime import date, timedelta
import demisto

def format_dt(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

def options_handler():
    parser = argparse.ArgumentParser(description='Utility for batch action on incidents')
    parser.add_argument('-u', '--user', help='The username for the login', required=True)
    parser.add_argument('-p', '--password', help='The password for the login', required=True)
    parser.add_argument('-s', '--server', help='The server URL to connect to', required=True)
    monthAgo = date.today() - timedelta(days=30)
    parser.add_argument('-f', '--filter', help='The filter query to chose the alerts, default is open incidents created in last month', default='(status:=0 or status:=1) and created:>%s' % format_dt(monthAgo))
    parser.add_argument('-m', '--page', help='The page we are working on', default=0, type=int)
    parser.add_argument('-n', '--size', help='The size per page', default=100, type=int)
    parser.add_argument('-a', '--action', help='The action to perform', default='close', choices=['close'])
    parser.add_argument('--closeReason', help='The close reason')
    parser.add_argument('--closeNotes', help='The close notes')
    parser.add_argument('--customFields', help='The json that includes the values for the custom fields')
    parser.add_argument('--playbook', help='The new playbook name')
    parser.add_argument('--type', help='The new type')
    parser.add_argument('--entry', help='The new entry data to create')
    parser.add_argument('-q', '--quiet', action='store_false', dest='verbose', default=True, help="don't use voice")
    options = parser.parse_args()
    global verbose
    verbose = options.verbose
    return options

def main():
    options = options_handler()
    c = demisto.DemistoClient(options.user, options.password, options.server)
    c.Login()
    incidents = c.SearchIncidents(options.page, 0, options.filter)
    print('using filter %s' %  options.filter)
    print('Total #incidents: %d, incidents going to be updated' % (incidents['total']))
    proceed = raw_input('OK to proceed (type y, yes or leave empty)? ')
    proceed = proceed.lower()
    if proceed == 'y' or proceed == 'yes' or proceed == '':
        if options.action == 'close':
            data = {'closeReason': options.closeReason, 'closeNotes': options.closeNotes, 'filter': {'page': options.page, 'size': options.size, 'query': options.filter}}
            data['all'] = True
            if options.customFields:
                data['CustomFields'] = json.loads(options.customFields)
            r = c.req('POST', 'incident/batchClose', data)
            if r.status_code != 200:
                raise RuntimeError('Error updating incidents - %d (%s)' % (r.status_code, r.reason))
            rj = json.loads(r.content)
            if rj['notUpdated'] > 0:
                print('Updated %d and could not update %d' % (rj['total']), rj['notUpdated'])
            else:
                print('Updated %d incidents' % rj['total'])

if __name__ == '__main__':
    main()