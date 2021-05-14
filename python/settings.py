#!/usr/bin/python3
# coding: utf8

import json, os

class settings:
    def __init__(self):
        configFile = '/config/config.json'
        with open(configFile,'r') as of:
            self.data = json.load(of)

    def api(self):
        api_info = self.data['API']
        return api_info

    def schedule(self):
        schedule_info = self.data['Schedule']
        return schedule_info

    def funding(self):
        funding_info = self.data['Funding']
        return funding_info

    def crypto(self):
        crypto_info = self.data['Crypto']
        return crypto_info

    def alerts(self):
        alerts_info = self.data['Alerts']
        return alerts_info