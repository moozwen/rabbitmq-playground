#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello, World')
print(" [x] sent 'Hello, World'")

connection.close()
