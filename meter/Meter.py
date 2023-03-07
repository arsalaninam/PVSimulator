#!/usr/bin/env python
import pika, random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='simulator')

while True:
    watt = random.randint(0, 9000)
    channel.basic_publish(exchange='', routing_key='simulator', body='{}'.format(watt))