#!/usr/bin/env python
import pika, sys, os, random, datetime

file = open("Output.txt", "a")

def callback(ch, method, properties, body):
        pv_value = random.uniform(0.0,4.0)
        body = body.decode("utf-8")
        sum_of_meter_and_pv = pv_value+(int(body)/1000)
        print(" [x] Received %r" % sum_of_meter_and_pv)

        file.write("\nMeter Power value : " + str(body) + "\tPV Power value : " + str(pv_value) + 
                   "\tSum of Powers : " + str(sum_of_meter_and_pv) + "\tTime Stamp " + str(datetime.datetime.now()) + "\n\n")

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='simulator')

    channel.basic_consume(queue='simulator', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)