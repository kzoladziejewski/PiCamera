import paho.mqtt.client as mqtt

class MQTTReceiverPicutre():

    def __init__(self):
        self.broker = "80.211.195.240"
        self.port = 1883

    def on_connect(client, userdata, rc):
        print("Connect with result code " + str(rc))
        client.subscribe('testowy')

    def on_message(client, userdata, msg):
        print("odebralem?")

        f = open('output.jpg', 'w')
        f.write(msg.payload)
        f.close()

    def go(self):
        client = mqtt.Client('control1')

        client.connect(self.broker, self.port, 60)
        client.on_message = self.on_message
        rc = 0
        while rc == 0:
            client.loop()

#
if __name__ == "__main__":
    MRP = MQTTReceiverPicutre()
    MRP.go()