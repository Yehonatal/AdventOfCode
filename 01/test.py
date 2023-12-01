import re 
def check(input_list):
    calibration_sum = 0    

    for line in input_list:
        num_list = re.findall(r"\d", line)
        num  = num_list[0] + num_list[-1]

        calibration_sum += int(num)

    return calibration_sum

def calibration(line):
    digits = [x for x in line if x.isdigit()]

    if len(digits): return int(digits[0]+digits[-1])
    else: return 0


    

# calibration_sum += check("1234")


print(check(["qxbhjmmqsixfkfn36three6"]))
print(check(["qweqw2e"]))


# print(calibration_sum)git pu