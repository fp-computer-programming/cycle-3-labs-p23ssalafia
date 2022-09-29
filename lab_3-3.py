#Author: Sean Salafia 9/28/22

from pickletools import read_unicodestring1
import random



x = random.randint(1,100)
print(x)

#seems to be a randdom number generated between 1 and 100

random.seed(55)
print(random.random())

#Prints a long string of random decimals depending on the seed with the first 2 digits resembling some form of similarity to the seed input.

random.randrange(0,100,2)
print(random.randrange(0,100,2))

#Prints an even number between 0 and 100.