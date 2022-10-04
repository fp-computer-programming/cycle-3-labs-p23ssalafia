#Author: Sean Salafia 9/30/22

import time
import math

x = time.time()
y = time.process_time_ns()

print(x)
print(y)

var_a = 2
print (var_a**2)

print(y)

#The code runs .031225 seconds after I press RUN, and executes instantly, completing the code in the same nanosecond

a = time.time()
b = time.perf_counter()

print(a)
print(b)

var_a = 2
print (var_a**2)

print(b)