#!/usr/bin/env python
import subprocess
from utils import *

targets = ["google.com"]
target = targets[0]

host = get_host()
count=0

# ADD A HEADER LINE TO THE .DAT file

while True:
	count+=1
	
	ping = subprocess.Popen(
	    ["ping", "-c", "10", "-i", "0.1", target],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	p_out, p_error = ping.communicate()

	date = subprocess.Popen(
	    ["date", "+%F %T"],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	d_out, d_error = date.communicate()

	# print '\n\ntimeT  : %s'%d_out
	#print 'timeE : %s\n'%d_error
	#print 'ping :\n %s'%p_out
	#print 'ping :\n %s'%select_ping_summary_line(p_out)
        ping_summary = summary_from_full_report(p_out)
	# print 'ping :\n %d %d %f'%ping_summary
	#print 'ping parsed:\n %d %d %s'%(unpack_ping(p_out))
	#print 'pingE:\n %s'%p_error

        # data_point = d_out.strip('\n') + ' ' + targer + ' ' + str(ping_summary[0]) + ' ' + str(ping_summary[1]) + ' ' + str(ping_summary[2])
        data_point = format_data_point(d_out, host, target, ping_summary)
        # print 'give you a debug show'
        print data_point
	fname = 'pings-DEV-'+d_out.split()[0]+'.dat'
	bufsize=9
	f = open(fname, 'a', buffering=bufsize) 	
	#f.write('\n\ntimeT : %s'%d_out)
	#f.write('timeE : %s\n'%d_error)
	#f.write('ping :\n %s'%p_out)
	f.write(data_point)

	if count%10==0:
		f.flush()

	f.close()
