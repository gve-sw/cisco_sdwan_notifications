# Cisco SD-WAN Notifications

A Flask application to automatically send emails following an alert in SD-WAN.

## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
* Cisco SD-WAN 
* Pythonanywhere 
* Python

## Solution Overview
![/IMAGES/image1.PNG](/IMAGES/flow.PNG)

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

#### Install the libraries :

```$ pip install -r requirements.txt```

## Setup: 

*Webhook Reciver*
1. Webhooks allow vManage to send alerts to an external system in real-time in the event of an alarm. 
You need a web server that will receive the webhooks from vManage. [Heroku](https://www.heroku.com/), [Pythonanywhere](https://www.pythonanywhere.com/) or [ngrok](https://ngrok.com/) (to run locally) are options that can be used. 

*Cisco SD-WAN*

2. Configure Webhooks on V-Manage. You can find the steps to configure Webhooks notifications [here.](https://www.cisco.com/c/en/us/support/docs/routers/sd-wan/214615-vmanage-configure-alarm-email-notificat.html)

*Notification-Email:*

3. Add the source email address and password which the email will be sent from to app.py. Additionally you will need to add the destination address. 
```
source_address = " "
password = " "
destination_address = " "
```
(Note for Google Users: 
By default  Google blocks sign-in attempts from apps which do not use modern security standards. You will need to [turn on the less secure app access](https://www.google.com/settings/security/lesssecureapps) to allow the app to access and send emails. 
Here is the [support page](https://support.google.com/accounts/answer/6010255?hl=en) for the details.)

*Notification-Cisco Webex:*

4. Create a Webex Chatbot from https://developer.webex.com/my-apps/new/bot.

5. Add your Bot Token to app.py.

```
bot_token = " "
```
6. Add the emails of Webex accounts to receive the notifications.

```
to = " "
```

## Usage

Host your appliaction on a server. E.g: Heroku and pythonanywhere are options which you can use. 

```
python app.py
```

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
