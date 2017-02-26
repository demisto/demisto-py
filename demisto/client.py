#!/usr/bin/env python2.7
import json
from requests import Session
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


class DemistoClient:
    XSRF_TOKEN_KEY = "X-XSRF-TOKEN"
    XSRF_COOKIE_KEY = "XSRF-TOKEN"

    # New client that does not do anything yet before the login
    def __init__(self, username, password, server):
        if not (username and password and server):
            raise ValueError("You must provide all three parameters")
        if not server.find('https://') == 0 and not server.find('http://') == 0:
            raise ValueError("Server must be a url (e.g. 'https://<server>' or 'http://<server>')")
        if not server[-1] == '/':
            server += '/'
        try:
            s = Session()
            r = s.get(server, verify=False)
        except InsecureRequestWarning:
            pass
        self.token = r.cookies[DemistoClient.XSRF_COOKIE_KEY]
        self.username = username
        self.password = password
        self.server = server
        self.session = s

    def req(self, method, path, data):
        h = {"Accept": "application/json",
             "Content-type": "application/json",
             DemistoClient.XSRF_TOKEN_KEY: self.token}

        try:
            if self.session:
                r = self.session.request(method, self.server+path, headers=h, verify=False, json=data)
            else:
                raise RuntimeError("Session not initialized!")
        except InsecureRequestWarning:
            pass
        return r

    def Login(self):
        data = {'user': self.username,
                'password': self.password}
        return self.req("POST", "login", data)

    def Logout(self):
        return self.req("POST", "logout", {})

    def CreateIncident(self, inc_name, inc_type, inc_severity, inc_owner, inc_labels, inc_details,custom_fields, **kwargs ):
        data = {"type": inc_type,
                "name": inc_name,
                "owner": inc_owner,
                "severity": inc_severity,
                "labels": inc_labels,
                "customFields": custom_fields,
                "details": inc_details}

        for e in kwargs:
            if e not in data:
                data[e] = kwargs[e]
        return self.req("POST", "incident", data)


    def SearchIncidents(self, page, size, query):
        data = {'filter': {'page': page, 'size': size, 'query': query, 'sort': [{'field':'id', 'asc': False}]}}
        r = self.req("POST", "incidents/search", data)
        if r.status_code != 200:
            raise RuntimeError('Error searching incidents - %d (%s)' % (r.status_code, r.reason))
        return r.json()
