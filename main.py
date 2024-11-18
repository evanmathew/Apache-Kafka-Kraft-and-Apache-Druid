import json
from faker import Faker
import time
import random
from kafka import KafkaProducer

faker = Faker()


def generate_data():
    '''
    This function generates/produces random data and sends it to kafka topic
    '''
    data ={}
    data['user_id'] = random.getrandbits(32)
    data['event_type'] = random.choice(['click', 'view', 'download'])
    data['country_code'] = faker.country_code()
    data['city'] = faker.city()
    data['device_type'] = random.choice(['desktop', 'mobile'])
    data['product_id'] = random.getrandbits(32)
    data['price'] = round(random.uniform(5.0, 500.0),2)
    data['quantity'] = random.randint(1, 100)
    data['timestamp'] = round(time.time())

    return data



if __name__ == '__main__':
    faker = Faker()
    topic_name='ecommerce_event_data'
    producer=KafkaProducer(
        bootstrap_servers=['localhost:29092','localhost:39092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    count=0
    # I am generating 50 records
    while count<50:
        data = generate_data()
        producer.send(topic_name, value=data)
        count+=1
        #print(f'Record Number {count}: {data}')
        producer.flush()
    