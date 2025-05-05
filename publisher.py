# publisher.py
import pika
 
class Publisher:
    def __init__(self, config):
        self.config = config
 
    def publish(self, queue_name, message):      
        connection = self.create_connection()
        channel = connection.channel()
        # Ensure queue exists
        channel.queue_declare(queue=queue_name)
        # Send message to the default exchange with queue name as routing key
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        print(f"[x] Sent message '{message}' to queue '{queue_name}'")
        connection.close()
 
    def create_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(
            host=self.config['host'],
            port=self.config['port']
        ))
 
config = {'host': 'localhost', 'port': 5672}
publisher = Publisher(config)
publisher.publish('test_queue', 'Hello via direct queue!')