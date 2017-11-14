import redis

channels = ['world', 'team']
r = redis.StrictRedis()

if __name__ == '__main__':
    pubsub = r.pubsub()
    map(pubsub.subscribe, channels)

    while True:
        for item in pubsub.listen():
            print item['data']