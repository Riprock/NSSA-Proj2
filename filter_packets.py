def filter(filename) :
	fsplit = filename.split('.')
	newfname = f"filtered{fsplit[0][4]}.{fsplit[1]}"
	print(newfname)
	with open(filename) as original:
		with open(newfname, "w") as new:
			for line in original:
				if "ICMP" in line and "unreachable" not in line:
					new.write(line)
	return newfname