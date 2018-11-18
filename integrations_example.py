#!/usr/bin/env python2.7

# example
# An example to retrieve all availabile integrations and commands for each
# Works on Demisto 2.5 onwards
#
# Author:       Slavik Markovich
# Version:      1.0
#

import argparse
import csv
import demisto


def p(what):
    if verbose:
        print(what)


def options_handler():
    parser = argparse.ArgumentParser(description='Integrations and commands')
    parser.add_argument(
        '-k', '--key', help='The API key to access the server', required=True)
    parser.add_argument(
        '-s', '--server', help='The server URL to connect to', required=True)
    parser.add_argument(
        '-q', '--quiet', action='store_false',
        dest='verbose', default=True, help="no extra prints")
    parser.add_argument(
        '-o', '--output', help='The output CSV file', default='integrations.csv')
    options = parser.parse_args()
    global verbose
    verbose = options.verbose
    return options


def main():
    options = options_handler()
    c = demisto.DemistoClient(options.key, options.server)
    integrationsResponse = c.req('GET', 'settings/integration-commands', None)
    if integrationsResponse.status_code != 200:
        raise RuntimeError('Error getting integration data - %d (%s)' %
                           (integrationsResponse.status_code, integrationsResponse.reason))
    integrations = sorted(integrationsResponse.json(),
                          key=lambda m: m['category'].lower() + '---' + m['name'].lower())
    with open(options.output, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                'Category', 'Product', 'ProductDescription', 'Command', 'CommandDescription'])
        writer.writeheader()
        for m in integrations:
            if 'commands' in m:
                for cmd in m['commands']:
                    writer.writerow({'Category': m['category'], 'Product': m['display'], 'ProductDescription': m['description'].encode('ascii', 'ignore'),
                                     'Command': cmd['name'], 'CommandDescription': cmd['description'].encode('ascii', 'ignore')})
            else:
                writer.writerow({'Category': m['category'], 'Product': m['display'],
                                 'ProductDescription': m['description'].encode('ascii', 'ignore')})


if __name__ == '__main__':
    main()
