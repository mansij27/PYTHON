from time import sleep
from threading import  *

class hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)

h1= hello()
sleep(1)
h2=Hi()

h1.start()
h2.start()

h1.join()
h2.join


print('BYE BYE')