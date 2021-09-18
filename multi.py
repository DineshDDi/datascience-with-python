'''
import _thread
import time

d = ['fd','kd','tr']
for x in d:
    print(x)
    try:
        _thread.sleep(2)
    except:
        print("error")

thread_1 = x
thread_2 = x

thread_1.start()
thread_2.start()
'''


'''
import _thread
import time

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
'''


"""
from threading import *
def th():
    for x in range(0,6):
        print("helllooooo")

t1 = Thread(target=th)
t1.start()
t1.join()
print("byeeeee")
t2 = Thread(target=th)
t2.start()
"""


"""
#child thread and main thread
from threading import *
def th():
    for x in range(0,6):
        print("helllooooo",current_thread().getName())

t1 = Thread(target=th)
t1.start()
t1.join()
print("byeeeee",current_thread().getName())
"""


"""
#using class multithreading
import threading
from threading import *
class a(threading.Thread):
    def run(self):
        for x in range(0,5):
            print("hiiiii",current_thread().getName())
obj = a()
obj.start()
obj.join()
print("byeee",current_thread().getName())
"""


"""
#without extend thread module
from threading import *
class a():
    def b(self):
        li = [1,2,3,4,6]
        for x in li:
            print("hii",x,current_thread().getName())

obj = a()
t1 = Thread(target=obj.b)
t1.start()
t1.join()
print("tq",current_thread().getName())
"""


'''
import threading
import time

def print_work_a():
    print('Starting of thread :', threading.currentThread().name)
    time.sleep(2)
    print('Finishing of thread :', threading.currentThread().name)

def print_work_b():
    print('Starting of thread :', threading.currentThread().name)
    print('Finishing of thread :', threading.currentThread().name)

a = threading.Thread(target=print_work_a, name='Thread-a', daemon=True)
b = threading.Thread(target=print_work_b, name='Thread-b')

a.start()
b.start()
'''

