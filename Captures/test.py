packets = []
ip = "192.168.100.1"
with open("filtered1.txt") as file:
    for line in file:
        packets.append(line.strip().split())
total = 0
count = 0
for i in range(0, len(packets), 2):
    if packets[i][8] == "request" and packets[i][2] == ip:
        total += (float(packets[i + 1][1]) - (float(packets[i][1])))
        count += 1
        avrg = (total / count) * 1000
print(avrg)