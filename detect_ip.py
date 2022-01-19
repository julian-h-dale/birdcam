import subprocess
import os
from sys import stdout


# set up email comms here

# detect the ip address

# send email comm
arg = 'ip route list'
proc = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
data = proc.communicate()
split_data = data[0].split()
# in orer to do the look up need to convert string 'src' to type Bytes
# ind = split_data[7]
# ipaddr = split_data[split_data.index('src') + 1]

print('ip address: ' + split_data[8].decode('utf-8'))