import sys
import json
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
from consumer import wait_response
from random import choice

if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])

    # Create Producer instance
    producer = Producer(config)

    # Produce data by selecting random values from these lists.
    topic = "calculator_requests"
    operations = ['sum', 'sub', 'mul', 'div', 'pow']
    values = [10,20,30,50]

    for _ in range(5):
        operation = choice(operations)
        value_a = choice(values)
        value_b = choice(values)
        calculate = {
            "operation": operation,
            "operator_1": value_a,
            "operator_2": value_b
        }

        file = json.dumps(calculate)
        print(f"Sent operation {operation} of {value_a} and {value_b}")
        producer.produce(topic, file, 'Items')
        print(f"Operation sent, waiting for result")
        print(f"The result is {wait_response()}.")

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
