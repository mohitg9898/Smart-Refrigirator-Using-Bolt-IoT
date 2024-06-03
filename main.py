from boltiot import Bolt, Sms
import conf
import json, time
import dtree



mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
previous_state = 0
N = True
while N:
    ldr_response = mybolt.analogRead('A0')
    pb_response = mybolt.digitalRead('1')

    ldr_data = json.loads(ldr_response)
    pb_data = json.loads(pb_response)
    print(ldr_data['value'])
    ldr_value = int(ldr_data['value'])
    print(pb_data['value'])
    pb_value = int(pb_data['value']) 

    present_state = dtree.MachineLearning_model(ldr_value)
    if previous_state != present_state or previous_state == present_state:
            try:
                if pb_value == 1 and ldr_value<=10:
                    print("Door is Closed")
                    led_state = mybolt.analogWrite('0','0')
                    response = sms.send_sms("Alert The Current door state is: CLOSE")
                    print("Status of SMS at Twilio is :" + str(response.status))

             
                else:
                    print("Door is open")
                    led_state = mybolt.analogWrite('0','255')
                    response = sms.send_sms("Alert The Current door state is: OPEN")
                    print("Status of SMS at Twilio is :" + str(response.status))

                previous_state = present_state

            except Exception as e:
                print("Error",e)
    time.sleep(10)
