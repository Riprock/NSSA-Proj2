from filter_packets import *
from packet_parser import *
from compute_metrics import *

fname = input("Please Specify the file name:")

if( "1" in fname):
    ip = "192.168.100.1"
elif( "2" in fname):
    ip = "192.168.100.2"
elif( "3" in fname):
    ip = "192.168.200.1"
elif( "4" in fname):
    ip = "192.168.200.2"
elif( "5" in fname):
    ip = "192.168.100.254"

packets = []
filtfile = filter(fname)
#print(filtfile)
parse(packets,filtfile)
compute(packets, ip, fname)
#Data size metrics 1-8 done