import sys
import time

from celery import Celery

celery = Celery('requeue', broker='amqp://guest@localhost//', backend='amqp')

@celery.task(ignore_result=False)
def add(a, b):
    time.sleep(3)
    return a + b

def main():

    result = add.delay(1, 2)

    if sys.argv[-1] == 'wait':
        print 'waiting...'
        time.sleep(4)
        # print result.get()
    else:
        while not result.ready():
            print 'checking'
            time.sleep(.5)

    print result.get()


if __name__ == '__main__':
    main()
