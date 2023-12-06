import sys 

Data = open(sys.argv[1]).read().strip()

lines = Data.split("\n")

nums = []
pairs = []

multi = 1

for line in lines:
    type_, values = line.split(":")
    for val in values.split("\n"):
        nums.append([int(x) for x in val.strip().split()])

for i in range(len(nums[0])):
    pairs.append([nums[0][i],nums[1][i]])

for pair in pairs:
    way = []
    t, d = pair[0], pair[1]

    for i in range(t):
        val = i * (t - i)
        
        if val > d:
            way.append(i)

    multi *= len(way)

print(multi)