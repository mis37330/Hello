import math
import random

xstr = "Encyclopedia"

ystr = ""

for elem in xstr:

    print(elem)

    ystr += elem

print("")

print(xstr, ystr)



xstr = "Encyclopedia"

Zstr = ""

for elem in xstr:

    print(elem)

    if elem == "c":

        Zstr += elem

print("")

print(xstr, Zstr)


xstr = "Encyclopedia"

Astr = ""

for elem in xstr:

    print(elem)

    if elem in ('c', 'e', 'a'):

        Astr += elem

print("")

print(xstr, Astr)




xstr = "Encyclopedia"

Bstr = ""

for elem in xstr:

    print(elem)

    if elem.isalpha():

        Bstr += elem

print("")

print(xstr, Bstr)

