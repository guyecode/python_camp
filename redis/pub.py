import sys
import redis
from faker import Faker


config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)
faker = Faker('zh_CN')

if __name__ == '__main__':
    channel = sys.argv[1]

    while True:
        name = faker.name()
        message = raw_input(u'Enter a message: '.encode('gbk'))
        if message.lower() == 'exit':
            break
        message = u'{name}: {message}'.format(**locals())

        r.publish(channel, message)
