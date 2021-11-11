
import random

astr = "Britannica"

alst = astr.split()

print(alst)


bstr = ""

for elem in alst:
    bstr += elem

print("")

if astr == bstr:
    print("Both strings are the same,:", astr)

if astr != bstr:
    print("The 2 strings are not the same. The are:", astr, bstr)

clst = ["Hip", "Hip", "Hooray!"]

for elem in clst:

    print(elem)

print("")

rg = random.randrange(10,20)

for ctr in range(rg):
    print(clst[0] + "," + clst[1] + ",")

print(clst[2])

print("")

dlst = ["one", "3", "apple", "tree", "7"]

print(dlst[2], dlst[3])

dlst[2] = "pear"

print("")

print(dlst[2], dlst[3])
