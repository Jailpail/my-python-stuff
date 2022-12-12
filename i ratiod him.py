import time
def helloworld():
    while(1):
     time.sleep(1)
     print("Hello world")
def hello():
    while(1):
     time.sleep(0.99)
     hello.counter += 1
     print(f"function helloworld has been ran for {hello.counter} seconds")
hello.counter = 0
from threading import Thread

t1 = Thread(target = helloworld)
t2 = Thread(target = hello)

t1.start()
t2.start()