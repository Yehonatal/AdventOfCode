import sys 

Data = open(sys.argv[1]).read().strip()

lines = Data.split('\n')

inst = lines[0]
inst = inst.replace("R", "1")
inst = inst.replace("L", "0")

print(inst)
nodes = {}

for line in lines[2:]:
    key = line.split("=")[0].strip()
    values = line.split("=")[1].strip().replace("(","").replace(")","").split(",")
    nodes[key] = [values[0], values[1].strip()]

def getInstruction(inst):
    for i in inst:
        yield int(i)

   
count = 1
key = 'AAA'
end = 'ZZZ'


def infinite_list_iteration(inst):
    index = 0
    while True:
        current_item = inst[index]
        yield current_item
        index = (index + 1) % len(inst)


iterator = infinite_list_iteration(inst)

while True:
    i = next(iterator)

    if nodes[key][int(i)] == end:
        break
    else:
        key = nodes[key][int(i)]
        count += 1
    

print(count)