import sys 
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


print(getPossibleGameTotal(data))