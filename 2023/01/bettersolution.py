import sys 
data = open(sys.argv[1]).read().strip()

p1 = 0 
p2 = 0 

for line in data.split('\n'):
    p1_digits = []
    p2_digits = []

    for i, char in enumerate(line):
        if char.isdigit():
            p1_digits.append(char)
            p2_digits.append(char)
        
        for j, val in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
            if line[i:].startswith(val):
                p2_digits.append(str(j+1))

    p1 += int(p1_digits[0]+p1_digits[-1])
    p2 += int(p2_digits[0]+p2_digits[-1])

print(p1)
print(p2)
    