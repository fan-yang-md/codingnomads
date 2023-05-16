# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
import datetime
print(datetime.datetime.now())
#print(str(datetime.date.today()))

import time
now = time.localtime()
print(time.strftime("%m/%d/%Y %H:%M:%S", now))