adict = {}

bdict = {"one" : 1, "two": 2, "three": 3, "four": 4}

print(bdict)

print(bdict["one"])

print(bdict["one"] + bdict["three"])

bdict["one"] = 8

print(bdict["one"] + bdict["three"])

print(bdict.keys())

cdict = {"alpha": "a", "beta": "b", "gamma" : "g"}

print(cdict)

print(cdict["beta"])

print(cdict["beta"] + cdict["gamma"])

ddict = {}

for ctr in range(2, 22):
    eval = ctr * 3
    ddict[ctr] = eval

print(ddict)

edict = {}

elst = ["Dave", "HAL", "Andi", "Jane", "Steve"]

flst =  [2343, 1232, 3434, 7658, 546]

for ctr in range(len(elst)):
        edict[elst[ctr]] = flst[ctr]

print(edict)

try:
    print(edict["Sammy"])

except:
    print("Sammy is not in that dictionary.")




