import sys 

Data = open(sys.argv[1]).read().strip()

lines = Data.split("\n")

lines = [line.strip() for line in lines if len(line)]

initial_seeds = [int(x) for x in lines[0].split(":")[1].split()]

def create_new_seeds(initial_seeds):
    new_seeds = []
    i, j = 0, 1

    while j <= len(initial_seeds):
        for k in range(initial_seeds[j]):
            new_seeds.append(initial_seeds[i] + k)
        i = j + 1
        j = i + 1


    return new_seeds

initial_seeds = create_new_seeds(initial_seeds) # part 2 just eats my RAM 🤧


maps = {}

lines = lines[1:]
i = 0
for j in range(len(lines)):
    if lines[j][0].isalpha():
        maps[lines[j].split()[0]] = []
        i = j
    else:
        if lines[i].split()[0] in maps:
            maps[lines[i].split()[0]].append(lines[j])

def returnList(key):
    list_ = [x.split() for x in list(maps[key])]
    list__ = []
    for x in list_:
        list__.append([int(y) for y in x])

    return list__

seed_to_soil_map = returnList("seed-to-soil")
soil_to_fertilizer_map = returnList("soil-to-fertilizer")
fertilizer_to_water_map =  returnList("fertilizer-to-water")
water_to_light_map =  returnList("water-to-light")
light_to_temperature_map =  returnList("light-to-temperature") 
temperature_to_humidity_map =  returnList("temperature-to-humidity")
humidity_to_location_map =  returnList("humidity-to-location") 

def convert_number(number, conversion_map):
    for dest_start, source_start, length in conversion_map:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number 

# Function to find the lowest location number
def find_lowest_location(initial_seeds):
    lowest_location = float('inf') 

    for seed in initial_seeds:
        soil = convert_number(seed, seed_to_soil_map)
        fertilizer = convert_number(soil, soil_to_fertilizer_map)
        water = convert_number(fertilizer, fertilizer_to_water_map)
        light = convert_number(water, water_to_light_map)
        temperature = convert_number(light, light_to_temperature_map)
        humidity = convert_number(temperature, temperature_to_humidity_map)
        location = convert_number(humidity, humidity_to_location_map)

        lowest_location = min(lowest_location, location)

    return lowest_location

print(find_lowest_location(initial_seeds))