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
import demisto

def options_handler():
    parser = argparse.ArgumentParser(description='Utility for batch action on incidents')
    parser.add_argument('-k', '--key', help='The API key to access the server', required=True)
    parser.add_argument('-s', '--server', help='The server URL to connect to', required=True)
    parser.add_argument('-n', '--name', help='Incident name', required=True)
    parser.add_argument('-t', '--type', help='Incident Type')
    parser.add_argument('-sev', '--severity', help='Incident Severity', default='Unknown', choices=['Critical', 'High', 'Medium', 'Low', 'Informational','Unknown'])
    parser.add_argument('-o', '--owner', help='Incident Owner')
    parser.add_argument('-d', '--details', help='Incident Details')
    parser.add_argument('-l', '--labels', help='Incident Labels, in the format [{"type":"t","value":"v"},{"type":"t2","value":"v2"}]')
    parser.add_argument('-c','--custom_fields', help='The json that includes the values for the custom fields, in the format {\'alertsource\': \'vc\',\'datetimecreated\': \'Wed, 15 Feb 2017 13:05:13 GMT\'}')
    options = parser.parse_args()

    return options


def severity_to_number(severity_str):
    return {
        'Critical': 4,
        'High': 3,
        'Medium': 2,
        'Low': 1,
        'Informational': 0.5,
        'Unknown': 0
    }[severity_str]

def main():
    options = options_handler()
    c = demisto.DemistoClient(options.key, options.server)
    labels = None
    if (options.labels is not None) and len(options.labels) > 0 :
        labels = json.loads(options.labels)
    fields = None
    if (options.custom_fields is not None) and len(options.custom_fields) > 0 :
        fields = json.loads(options.custom_fields)
    r = c.CreateIncident(options.name, options.type, severity_to_number(options.severity), options.owner, labels, options.details, fields)
    print(r)

if __name__ == '__main__':
    main()