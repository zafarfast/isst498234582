# ISS Tracker


## Table of Contents
- Description
- GitGub Link
- Technologies used
- Pre-requisites
- How to use
- Screenshots


## Description
This program utilizes the requests library to fetch real-time ISS location data from the "http://api.open-notify.org/iss-now.json" API. It also uses the twilio library to send SMS messages. Here's a high-level overview of the program's functionality:

The program first collects the user's location (latitude and longitude) or allows the user to input their location manually.

It continuously fetches the ISS's current location from the Open Notify API and compares it to the user's location.

When the ISS is above the user's location (within a certain threshold), the program sends an SMS notification using the Twilio API.


## GitHub Link
https://github.com/zafarfast/isst498234582

## Technologies used:
- Requests module
- Twilio module
- Twilio account

## Pre-requisites

- Twilio account: To run the program you will need Account SID and Auth Token. This can be obtained by registering with Twilio at https://www.twilio.com/try-twilio

- Location co-ordinates: You can obtain the co-ordiantes of you location on Google map.  A details guide can be found here > https://www.howtogeek.com/689097/how-to-get-latitude-and-longitude-coordinates-from-google-maps/

## How to use

Once you have the Account SID, Auth Token and Twilio mobile number, put it in the main.py file and run. 

NOTE: The Account SID, Auth Token and Twilio mobile number in the main.py file are not valid so it won't work unless you replace them with your own account.

## How to run

This program is made to run continously so that it can keep monitoring ISS's location. Running it on the personal computer is not practical and therefore it needs to be run on the cloud or cloud based IDE such as PythonAnywhere.

PythonAnywhere is an online platform and cloud-based Integrated Development Environment (IDE) designed specifically for Python programming and web hosting. It allows Python developers to write, run, and host Python applications, websites, and web apps in a browser-based environment. 

You can create a free acconut here > https://www.pythonanywhere.com/registration/register/beginner/

Here is how you can deploy your app on PythonAnywhere > https://www.youtube.com/watch?v=wbAhmGFwZ-g

## Screenshots

![alt text](notification_screenshot.jpeg)


