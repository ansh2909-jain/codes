import pika
import sys
 
class Subscriber:
    def __init__(self, queue_name, config):
        self.queue_name = queue_name
        self.config = config
        self.connection = self._create_connection()
 
    def __del__(self):
        self.connection.close()
 
    def _create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port']
        ))
 
    def on_message_callback(self, channel, method, properties, body):
        print(f"Received message: {body.decode()}")
 
    def setup(self):
        channel = self.connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_consume(queue=self.queue_name,
                              on_message_callback=self.on_message_callback,
                              auto_ack=True)
        print(f"[*] Waiting for messages in queue '{self.queue_name}'. To exit press CTRL+C")
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
 
config = {'host': 'localhost', 'port': 5672}
 
if len(sys.argv) < 2:
    print('Usage: ' + __file__ + ' <QueueName>')
    sys.exit()
else:
    queue_name = sys.argv[1]
    subscriber = Subscriber(queue_name, config)
    subscriber.setup()