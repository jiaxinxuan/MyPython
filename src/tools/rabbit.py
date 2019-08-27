import pika


username = 'quanwai'
pwd = 'quanwai'
user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='101.132.185.195', port=5672, credentials=user_pwd,
                                                               virtual_host='/'))


def consumer(message):
    assert isinstance(message, object)
    print(message)


def producer():
    channel = connection.channel()
    channel.basic_publish(exchange='Alarm.BU.Channel', routing_key='Alarm.BU.Channel.Order',
                          body='{}')
    connection.close()
    print("test")


if __name__ == '__main__':
    producer()
