#!/usr/bin/env python2.7

# example
# An example of helper utility to upload files to the war room
#
#
# Author:       Ronald Eddings
# Version:      1.0
#

import json
import argparse
import demisto

def options_handler():
    parser = argparse.ArgumentParser(description='Utility for uploading files to the war room')
    parser.add_argument('-k', '--key', help='The API key to access the server', required=True)
    parser.add_argument('-s', '--server', help='The server URL to connect to', required=True)
    parser.add_argument('-i', '--id', help='Incident ID', required=True)
    parser.add_argument('-f', '--filepath', help='File Path', required=True)
    options = parser.parse_args()

    return options

def main():
    options = options_handler()
    client = demisto.DemistoClient(options.key, options.server)
    response = client.UploadFileToWarroom(options.id, options.filepath)
    print(response)

if __name__ == '__main__':
    main()
