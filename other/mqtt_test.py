import paho
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-1'

# ClientId不能重复，也可不传入
mqtt_client1 = mqtt_client.Client(client_id="python-mqtt-1")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test")


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))
    # 消息处理


def publish(msg):
    result = mqtt_client1.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print("Send `{}` to topic `{}`".format(msg, topic))
    else:
        print("Failed to send message to topic {}".format(topic))


# 匿名登录不需要设置
mqtt_client1.username_pw_set("xter", "hhhhllll")  # 必须设置，否则会返回「Connected with result code 4」
mqtt_client1.on_connect = on_connect
mqtt_client1.on_message = on_message
mqtt_client1.connect("192.168.10.248", 1883, 60)
# 订阅主题
mqtt_client1.subscribe("test")
mqtt_client1.loop_forever()