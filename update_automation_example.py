#!/usr/bin/env python3

import argparse
import os
import sys
import json
import unittest

import demisto


def options_handler():
    parser = argparse.ArgumentParser(
        description='an example of update automation by demisto.client',
        usage="""
  update automation example:
    %(prog)s $DEMISTO_API_KEY https://demisto.example.com/ -f my_automation_script.py [-n automation_name]
  unit test of demisto.client.(Search|Load|Update|Save|Delete)Automation:
    %(prog)s $DEMISTO_API_KEY https://demisto.example.com/ -t"""
    )
    parser.add_argument(
        'key', help='The API key to access the server')
    parser.add_argument(
        'url', help='Base URL of API')
    parser.add_argument(
        '-t', '--test', help='run unit test instead of updating automation', action='store_true')
    parser.add_argument(
        '-n', '--name', help='automation name')
    parser.add_argument(
        '-f', '--file', nargs='?', type=argparse.FileType('r'),
        help='automation script name(.py or .js)',
        default=sys.stdin)
    options = parser.parse_args()
    if options.name is None:
        if options.file.name == '<stdin>':
            if options.test:
                options.name = "test"
            else:
                raise RuntimeError(
                    'Error parsing options - name is required')
        else:
            options.name = os.path.splitext(
                os.path.basename(options.file.name))[0]
    return options


class TestAutomation(unittest.TestCase):
    """
    tests for search/delete/update/load/save automation.
    demisto server is required.
    if automation cls.name is already exist at setUpClass, this will throw RuntimeError.
    """
    @classmethod
    def setUpClass(cls):
        automations = cls.client.SearchAutomation("name:{}".format(cls.name))
        if len(automations["scripts"]) > 0:
            raise RuntimeError("automation {} is already exist. test is cancelled. use another name, or delete it.")

    def setUp(self):
        automation = {
            "name": self.name,
            "script": "demisto.results('Hello, world!')"
        }
        automations = self.client.SaveAutomation(automation)
        self.id = automations["scripts"][0]["id"]

    def tearDown(self):
        if self.id:
            automation = {
                "name": self.name,
                "id": self.id
            }
            self.client.DeleteAutomation(automation)
            self.id = None

    def test_search(self):
        automations = self.client.SearchAutomation("name:{}".format(self.name))
        self.assertIn("scripts", automations)
        self.assertEqual(len(automations["scripts"]), 1)
        self.assertIn("id", automations["scripts"][0])

    def test_delete(self):
        automation = {
            "name": self.name,
            "id": self.id
        }
        client.DeleteAutomation(automation)
        self.id = None
        automations = self.client.SearchAutomation("name:{}".format(self.name))
        self.assertIn("scripts", automations)
        self.assertEqual(len(automations["scripts"]), 0)

    def test_save_new(self):
        automation = {
            "name": self.name,
            "id": self.id
        }
        client.DeleteAutomation(automation)
        automation = {
            "name": self.name,
            "script": "demisto.results('Hello, world!')"
        }
        automations = self.client.SaveAutomation(automation)
        self.assertIn("scripts", automations)
        self.assertEqual(len(automations["scripts"]), 1)
        self.assertIn("id", automations["scripts"][0])
        self.id = automations["scripts"][0]["id"]

    def test_load(self):
        automation = self.client.LoadAutomation(self.id)
        self.assertIn("id", automation)
        self.assertEqual(automation["id"], self.id)

    def test_update(self):
        script = "demisto.results('Hello, world!!!!')"
        automations = self.client.UpdateAutomation(
            None, self.name, script=script)
        self.assertIn("scripts", automations)
        self.assertEqual(len(automations["scripts"]), 1)
        self.assertIn("version", automations["scripts"][0])
        self.assertEqual(automations["scripts"][0]["version"], 2)


if __name__ == '__main__':
    options = options_handler()
    client = demisto.DemistoClient(options.key, options.url)
    if options.test:
        TestAutomation.name = options.name
        TestAutomation.client = client
        if sys.argv:
            del sys.argv[1:]
        unittest.main()
        sys.exit(0)
    script = options.file.read()
    automations = client.UpdateAutomation(None, options.name, script=script)
    print(json.dumps(automations))
