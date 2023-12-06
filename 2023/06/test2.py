t = 15
d = 40

way = []
for i in range(t):
    # 2 * (7-2)
    val = i * (t - i)
    
    if val > d:
        way.append(i)


print(way)