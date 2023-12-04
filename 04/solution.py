import sys 
import collections
Data = open(sys.argv[1]).read().strip()

def getPoints(Data):
    total = 0
    for line in Data.split("\n"):
        
        point = 0
        card_Id, sets = line.split(":")
        win, nums = sets.split("|")
        intersect = collections.Counter([x.strip() for x in win.split()]) & collections.Counter([x.strip() for x in nums.split()])

        for _ in list(intersect):
            if point < 1:
                point = 1
            else:
                point *= 2


        total += point

    return total

def getAllCards(Data):
    winning_cards = collections.defaultdict(int)
    for i, line in enumerate(Data.split("\n")):
        winning_cards[i] += 1
        
        card_Id, sets = line.split(":")
        win, nums = sets.split("|")
        intersect = collections.Counter([x.strip() for x in win.split()]) & collections.Counter([x.strip() for x in nums.split()])

        for j in range(len(list(intersect))):
            winning_cards[i + 1 + j] += winning_cards[i]

        

    return sum(winning_cards.values())


print(getPoints(Data))
print(getAllCards(Data))