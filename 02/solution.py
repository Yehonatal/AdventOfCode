import sys 
import math

data = open(sys.argv[1]).read().strip()

def getPossibleGameTotal(data):
    games_id_total = 0
    for line in data.split("\n"):
        status = True 
        id_, line = line.split(":")
        for sets in line.split(";"):
            for set_ in sets.split(','):
                n, color = set_.split()
                if int(n) > {"red":12, "blue":14, "green":13}.get(color, 0):
                    status = False 

        if status:
            games_id_total += int(id_.split()[-1])


    return games_id_total


def getMinimumSetLimit(data):
    minimum_set_total = 0
    for line in data.split("\n"):
        id_, line = line.split(":")

        max_value = {"red":0, "blue":0, "green":0}
        for sets in line.split(";"):
            for set_ in sets.split(","):
                n, color = set_.split()

                if int(n) > max_value.get(color):
                    max_value[color] = int(n)
        
        minimum_set_total += math.prod(list(max_value.values()))


    return minimum_set_total


print(getPossibleGameTotal(data))
print(getMinimumSetLimit(data))