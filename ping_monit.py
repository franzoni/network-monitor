#!/usr/bin/env python
import subprocess
from utils import *

host = "www.google.com"

count=0

while True:
	count+=1
	
	ping = subprocess.Popen(
	    ["ping", "-c", "10", "-i", "0.1", host],
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

	print '\n\ntimeT  : %s'%d_out
	print 'timeE : %s\n'%d_error
	print 'ping :\n %s'%p_out
	print 'ping parsed:\n %s'%p_out
	print 'pingE:\n %s'%p_error

	fname = 'pings-'+d_out.split()[0]+'.dat'
	bufsize=9
	f = open(fname, 'a', buffering=bufsize) 	
	f.write('\n\ntimeT : %s'%d_out)
	f.write('timeE : %s\n'%d_error)
	f.write('ping :\n %s'%p_out)
	f.write('pingE:\n %s'%p_error)

	if count%10==0:
		f.flush()

	f.close()
