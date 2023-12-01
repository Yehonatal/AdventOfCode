import sys 

calibration_sum = 0

def calibration(line):
    digits = [x for x in line if x.isdigit()]

    if len(digits): return int(digits[0]+digits[-1])
    else: return 0



if (len(sys.argv) != 2):
    sys.exit(1)


file_path = sys.argv[1]

try:
    with open(file_path, "r") as file:
        for line in file:
            calibration_sum += calibration(line.strip())

except FileNotFoundError:
    print("File not Found")
except Exception as e:
    print("Error", e)


# print(content)
print(calibration_sum)