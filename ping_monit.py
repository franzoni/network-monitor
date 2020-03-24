#!/usr/bin/env python
import subprocess
from utils import *

targets = ['google.com','letemps.ch']
header  = 'date time host target transm received percdrop\n\n'
host    = get_host()
count   = 0
out_dir = get_outout_path()

while True:

	count+=1

        for target in targets:
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

                ping_summary = summary_from_full_report(p_out)
                data_point = format_data_point(d_out, host, target, ping_summary)

                if count%30 ==0:
                        print data_point

	        bufsize=9
                fname  = 'pings-'+host+'-'+d_out.split()[0]+'.dat'
                fwpath = out_dir+fname
                f = open(fwpath, 'a', buffering=bufsize)
                if count==1:
                        f.write(header)
	        f.write(data_point)

        
	if count%10==0:
		if count%120 ==0:
                        count=0
		f.flush()

	f.close()
