#!/usr/bin/python3
# coding: utf8

import requests
import json
from discord import Webhook, RequestsWebhookAdapter
import http.client, urllib

class alert_module:

    ALERT_CHANNEL_DISCORD = "discord"
    ALERT_CHANNEL_PUSHOVER = "pushover"
    ALERT_CHANNEL_NONE = "none"

    def __init__(self):
        configFile = '/config/config.json'
        with open(configFile,'r') as of:
            self.data = json.load(of)
    
    def send(self, alert_msg=""):
        alert_info = self.data['Alerts']
        for alert_data in alert_info:
            if alert_data['Alert-Channel'] == 'discord':
                webhook = Webhook.from_url(alert_data['Discord-Webhook'], adapter=RequestsWebhookAdapter())
                webhook.send(alert_msg)
            elif alert_data['Alert-Channel'] == 'pushover':
                webhook = http.client.HTTPSConnection("api.pushover.net:443")
                webhook.request("POST", "/1/messages.json",
                    urllib.parse.urlencode({
                        "token": alert_data['Pushover-API-Token'],
                        "user": alert_data['Pushover-User-Key'],
                        "message": alert_msg
                    }), { "Content-type": "application/x-www-form-urlencoded" })
                webhook.getresponse()
            elif alert_data['Alert-Channel'] == 'pushcut':
                webhook = http.client.HTTPSConnection("api.pushcut.io:443")
                webhook.request("POST", "/v1/notifications/" + alert_data['Pushcut-Notification-Name'],
                    urllib.parse.urlencode({
                        "text": alert_msg
                    }), { "Content-type": "application/x-www-form-urlencoded", "API-Key": alert_data['Pushcut-API-Key'] })
                webhook.getresponse()
