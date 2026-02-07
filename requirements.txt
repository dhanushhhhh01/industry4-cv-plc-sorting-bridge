import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    color = msg.payload.decode()
    # Here you would trigger your PLC tag via Modbus or OPC-UA
    print(f"Commanding PLC: Activate Piston for {color}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("factory/sorter/color")
client.loop_forever()
