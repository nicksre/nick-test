import time
import sys

time1 = sys.argv[1].strip('"')
time2 = sys.argv[2].strip('"')
a = time.strptime(time1, '%Y-%m-%dT%H:%M:%S.000Z')
b = time.strptime(time2, '%Y-%m-%dT%H:%M:%S.000Z')

a = time.mktime(a)
b = time.mktime(b)

c = b - a

print(c)