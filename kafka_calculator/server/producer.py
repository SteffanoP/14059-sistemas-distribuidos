import json
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer

def send(result):
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
    topic = "calculator_results"
    result = json.dumps({'result': result})
    producer.produce(topic, result, 'Items')

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
