# coding: utf-8

"""

"""

import sys
import random
import time
from datetime import datetime, timedelta
import redis
from faker import Faker


f = Faker()
r = redis.Redis()
DEADLINE = datetime.now() + timedelta(hours=1)


def exam(course, students=50):
    for i in range(students):
        name = f.name() 
        time_remaining = (DEADLINE - datetime.now()).total_seconds()
        score = '%s.%s' % (random.randint(80, 100), str(time_remaining).replace('.', ''))
        print i, course, name, score
        r.zadd(course, name , score)

        time.sleep(0.1)



if __name__ == '__main__':
    exam('English')