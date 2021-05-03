def parse(packets, newfname) :
	with open(newfname) as file:
		for line in file:
			packets.append(line.strip().split())