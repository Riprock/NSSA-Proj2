def compute(packets, ip , fname):
	nodes = fname.split('.')[0]
	a1 = request_bytes_sent(packets,ip)
	a2 = request_bytes_recv(packets,ip)
	a3 = request_data_sent(packets,ip)
	a4 = request_data_recv(packets,ip)
	a5 = requets_throughput(packets, ip, a1)
	a6 = avgHop(packets)
	print(f'{a1} {a2} {a3} {a4} {a5} {a6}')

def numOfEchoRequestsSent(packets, ipadd) :
    totalPackets = 0
    for packet in packets:
        if packet[8] == "request" and packet[2] == ipadd:
            totalPackets += 1
    return totalPackets

def numOfEchoRequestsReceived(packets, ipadd) :
    totalPackets = 0
    for packet in packets:
        if packet[8] == "request" and packet[3] == ipadd:
            totalPackets += 1
    return totalPackets

def numOfEchoRepliesSent(packets, ipadd) :
    totalPackets = 0
    for packet in packets:
        if packet[8] == "reply" and packet[2] == ipadd:
            totalPackets += 1
    return totalPackets

def numOfEchoRepliesReceived(packets, ipadd) :
    totalPackets = 0
    for packet in packets:
        if packet[8] == "reply" and packet[3] == ipadd:
            totalPackets += 1
    return totalPackets

def averageReplyDelay(packets, ipadd) :
    total = 0
    count = 0
    # start at beginning of list, go to end of list, then step by 2 indexes to get 
    # a request and reply at a time for every time you loop through list.
    for i in range(0, len(packets), 2):
        if packets[i][8] == "request" and packets[i][3] == ipadd:
            total += ( float(packets[i + 1][1]) - (float(packets[i][1])) )
            count += 1
            # Average converted to micros seconds
            average = (total / count) * 1000000
            # Time = Request - reply
            # Request = packets[i+1][1]
            # Reply = packets[i][1]
    return round(average, 2)

def request_bytes_sent(packets,ip):
	num_bytes = 0
	for packet in packets:
		if ip in packet[2] and "request" in packet[8]:
			num_bytes += int(packet[5])
	return num_bytes 

def request_bytes_recv(packets,ip):
	num_bytes = 0
	for packet in packets:
		if ip in packet[2] and "reply" in packet[8]:
			num_bytes += int(packet[5])
	return num_bytes 

def request_data_sent(packets,ip):
	num_bytes = 0
	for packet in packets:
		if ip in packet[2] and "request" in packet[8]:
			num_bytes = num_bytes +  int(packet[5]) - 42
	return num_bytes 

def request_data_recv(packets,ip):
	num_bytes = 0
	for packet in packets:
		if ip in packet[2] and "reply" in packet[8]:
			num_bytes = num_bytes +  int(packet[5]) - 42
	return num_bytes 


def requets_throughput(packets, ip, request_bytes):
	count = 0
	for i in range(0, len(packets), 2):
		if ip in packets[i][2] and "request" in packets[i][8]:
			count = count + (float(packets[i + 1][1]) - float(packets[i][1]))
	return round((request_bytes/count)/1000, 1)

def hop_avg(packets):
	total_hops = 0
	count_requests = 0
	for i in range(0, len(packets), 2):
		if "request" in packets[i][8]:
			count_requests += 1
			total_hops = total_hops + (129 - int(packets[i][11].split('=')[1]))
		else:
			continue
	return round((float(total_hops) / float(count_requests)), 2)

