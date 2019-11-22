from math import *
from random import *
from time import *
from os import *


def pyt2(x,y):
  return sqrt(x*x+y*y)

def pyt3(x,y,z):
  return sqrt(x*x+y*y+z*z)

def pytn(x):
  r=0
  for i in range(len(x)):
    r+=x[i]**2
  return sqrt(r)
