import sys 
import collections
Data = open(sys.argv[1]).read().strip()

winning_cards = collections.defaultdict(int)
for i, line in enumerate(Data.split("\n")):
    winning_cards[i] += 1

    card_Id, sets = line.split(":")
    win, nums = sets.split("|")
    intersect = collections.Counter([x.strip() for x in win.split()]) & collections.Counter([x.strip() for x in nums.split()])

    for j in range(len(list(intersect))):
        winning_cards[i + 1 + j] += winning_cards[i]

    
# print(winning_cards)

print(sum(winning_cards.values()))