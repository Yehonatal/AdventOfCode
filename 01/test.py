import re 
def check(input_list):
    calibration_sum = 0    

    for line in input_list:
        num_list = re.findall(r"\d", line)
        num  = num_list[0] + num_list[-1]

        calibration_sum += int(num)

    return calibration_sum
    
    

# calibration_sum += check("1234")


print(check(["qxbhjmmqsixfkfn36three6"]))
print(check(["qweqw2e"]))


# print(calibration_sum)