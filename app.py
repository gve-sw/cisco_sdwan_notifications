"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
import json

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
bot_token = " "
api = WebexTeamsAPI(access_token=bot_token)


destination_address = " "
source_address = " "
password = " "

to =" "


@app.route('/alert', methods=['POST'])
def alert_received():
    try:
        content = json.loads(request.data)

        alarm_msg = content['message']
        sys_ip = content['values'][0]['system-ip']
        host_name = content['values'][0]['host-name']
        severity = content['severity']
        try:
            # If there is a site id that is returned
            site_id = content['values'][0]['site-id']
            alert_complete_message = alarm_msg + ' for device ' + sys_ip + ' with site id ' + site_id + ' with hostname ' + host_name

        except:
            alert_complete_message = alarm_msg + ' for device ' + sys_ip + ' with hostname ' + host_name

        subject = severity + ': Sd-wan alert'
        send_email(destination_address, source_address, password, subject, alert_complete_message)
        resp = api.messages.create(toPersonEmail=to, text=alert_complete_message)
        return severity

    except:
        error_message = "Could not parse payload: payload error"
        resp = api.messages.create(toPersonEmail=to, text=error_message)
        print(resp)
        return "Could not parse payload: payload error"


def send_email(destination_address, source_address, password, subject, message):
    email_message = MIMEMultipart()
    email_message['subject'] = subject
    email_message['From'] = source_address
    email_message['To'] = destination_address
    message_body = MIMEText(message, 'html')
    email_message.attach(message_body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(source_address, password)
    server.sendmail(source_address, destination_address, email_message.as_string())
    server.quit()
    return "sent the email"
