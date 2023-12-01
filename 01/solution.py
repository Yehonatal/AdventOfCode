import re
import sys 


def problemOne(line):
    cal_sum = 0    

    for line in input_list:
        num_list = re.findall(r"\d", line)
        num  = num_list[0] + num_list[-1]

        cal_sum += int(num)

    return cal_sum


def problemTwo(input_list):
    nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    cal_sum = 0    
    new_list = []

    for line in input_list:
        pattern = r"(one|two|three|four|five|six|seven|eight|nine|\d)"
        draft = list(match.group()
                for start in range(len(line))
                for match in [re.match(pattern, line[start:])]
                if match)
        
        new_list = [nums[x] if x in nums else x for x in draft]
        num  = new_list[0] + new_list[-1]

        cal_sum += int(num)
        
    return cal_sum


# Parse input and create a list 
if (len(sys.argv) != 2):
    sys.exit(1)


file_path = sys.argv[1]

try:
    with open(file_path, "r") as file:
        input_list = file.read().split("\n")

except FileNotFoundError:
    print("File not Found")
except Exception as e:
    print("Error", e)

# use the list
print(problemOne(input_list))
print(problemTwo(input_list))