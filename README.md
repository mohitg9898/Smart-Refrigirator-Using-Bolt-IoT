# Smart-Refrigirator-Using-Bolt-IoT

# Problem Statement
In the era of smart homes, enhancing household appliances with IoT capabilities has become essential for convenience, efficiency, and safety. One such innovation is the development of a smart refrigerator that can detect and notify the user of its door status. This project aims to create a proof of concept for a smart refrigerator lighting system using the Bolt IoT platform. The system will utilize data from a Light Dependent Resistor (LDR) and a push button to determine and communicate the state of the refrigerator door.

# Objective
To design and implement a smart lighting system for a refrigerator that:

1.Detects whether the refrigerator door is open or closed using an LDR and a push button.
2.Sends an SMS notification to the user whenever the state of the door changes.

# Functional Requirements
1.Data Collection:
     Use the LDR to measure light intensity inside the refrigerator.
     Use the push button to determine if the door is physically pressed (closed) or released (open).
2.State Determination:
     Door Open: High light intensity (bright) and button released.
     Door Closed: Low light intensity (dark) and button pressed.
3.Notification System:
     Send an SMS with the current state of the door whenever there is a change in its status.

# Things used in this project
# Hardware components
1.Bolt IoT Bolt Wifi Module

2.LDR Sensor

3.Resistor 10k ohm

4.Breadboard

5.Pushbuttom switch

6.Jumper wires 
# Software apps and online services
1.Bolt IoT Bolt Cloud

2.Twilio SMS service

3.Replit


# Gathering all required components

<!-- wp:paragraph -->
<p>These are the components required</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1. Bolt WiFi Module</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":24179,"width":399,"height":149,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2024/06/b.jpeg" alt="" class="wp-image-24179" width="399" height="149"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>2. LDR (Light Dependent Resistor)</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":24178,"width":210,"height":130,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2024/06/ldr.jpeg" alt="" class="wp-image-24178" width="210" height="130"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>3. PushButton</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":24180,"width":186,"height":186,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2024/06/bb.jpeg" alt="" class="wp-image-24180" width="186" height="186"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>4. Resistor 10K</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":24181,"width":165,"height":165,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2024/06/111.jpeg" alt="" class="wp-image-24181" width="165" height="165"/></figure>
<!-- /wp:image -->


# Step 1: Building the circuit
Ensure that the Bolt Module is not powered on while connecting the circuit to prevent short circuits.
Connect the LDR:
One end to the A0 (analog) pin.
The other end to the 3.3V pin.
Place a 10K ohm resistor between the GND and A0 pin, forming a series connection with the LDR.
Connect the Push Button:
One end to the 1 (digital) pin.
The other end to the 3.3V pin.
Place a 10K ohm resistor between the GND and 1 pin, forming a series connection with the push button.
After making these connections, you can safely power on the Bolt Module and continue with the configuration.

This image has an empty alt attribute; its file name is Screenshot-617.png
Circuit

# Step 2: Testing Circuit
To test the circuit, we need to import the required libraries and check the functionality of the LDR and push button.

# Create conf.py with Bolt IoT configurations
API_KEY = 'Your_Bolt_Cloud_API_Key'
DEVICE_ID = 'Your_Bolt_Device_ID'
﻿
# Import Libraries
First, import the necessary libraries in your Python script.

from boltiot import Bolt, Email
import conf
import json, time
# Initialize Bolt
mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
# Testing LDR
Read the value from the LDR connected to the A0 pin and print it.

ldr_response = mybolt.analogRead('A0')
ldr_data = json.loads(ldr_response)
print(ldr_data['value'])
ldr_value = int(ldr_data['value'])
# Testing Push Button
Read the value from the push button connected to the digital pin 1 and print it.

pb_response = mybolt.digitalRead('1')
pb_data = json.loads(pb_response)
print(pb_data['value'])
pb_value = int(pb_data['value'])

# Step 3: Software Programming
1.Log in to Bolt Cloud and note the ID of your Bolt WiFi Module.
2.Click on the API Tab, and under the "Generate Key" section, click on Enable to get your API Key.
3.Sign up on Twilio and generate an API Key, SID, and a Twilio phone number.
4.Use Repl.it for running the Python script.Alternatively, you can run Python files on a Digital Ocean droplet or an Ubuntu server virtual machine.
5.Store all credentials related to Twilio and Bolt IoT in conf.py.Replace placeholder values with your actual credentials.
6.Implement the logic in main.py.
7.Create dtree.py and implement the decision tree model.You can find the code and dataset in the provided GitHub link.
8.The script will send an SMS through the Twilio API when the door state changes from closed to open and vice versa.
9.Run main.py on Repl.it or your chosen environment to start monitoring the refrigerator door and receiving SMS notifications.

# Code 
This  system designed to predict the state of a refrigerator door using machine learning techniques. Initially, essential dependencies such as pandas, numpy, and scikit-learn are installed. The core of the system lies in a machine learning model, Decision Tree classifier, trained on a dataset containing sensor readings and door states. The model's predictions are then used to determine the state of the door in real-time.

The system incorporates a logical flow to handle various scenarios. If a push button is pressed, indicating the door is closed, the system reacts accordingly. Otherwise, the predicted door state from the machine learning model is considered. When a change in door state is detected, appropriate actions are taken, including printing messages, and sending sms alerts using the Twilio API. Exception handling ensures graceful handling of errors, if any, during the process.

This integration of machine learning with real-time monitoring and response mechanisms demonstrates an effective approach to anomaly detection and control in IoT applications like refrigerator door monitoring.

# Conclusion
This project will deliver a smart refrigerator lighting system that enhances user awareness and interaction with their appliance. By leveraging the Bolt IoT platform and simple sensors, the system will effectively monitor the refrigerator door status and provide real-time notifications, ensuring users are promptly informed of any changes. It provides crucial monitoring for cold storage units, particularly in drug manufacturing industries, ensuring precise oversight of refrigerator activities and enhancing storage operations' reliability.

