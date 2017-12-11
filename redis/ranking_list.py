# coding: utf-8
import time
import random
import redis
from datetime import datetime, timedelta
import faker

r = redis.Redis()
faker = faker.Faker('zh_CN')
DEADLINE = datetime.now() + timedelta(hours=1)


def exam(course, students=50):
    print '%s exam started...' % course
    for i in range(students):
        name = faker.name()
        time_remaining = (DEADLINE - datetime.now()).total_seconds()
        score = '%s.%s' % (random.randint(60, 100),
                str(time_remaining).replace('.', ''))
        r.zadd(course, name, score)
        print('%s: %s' % (name, score))
        time.sleep(0.1)

def top(course, rank_range=10):
    stus = r.zrevrange('English', 0, 10, withscores=True)
    for i, s in enumerate(stus):
        print i + 1, s[0], s[1] 


if __name__ == '__main__':
    courses = ['English', 'Chinese', 'Math']
    for course in courses:
        exam(course, students=50)
        top(course)

