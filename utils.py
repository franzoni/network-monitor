def summary_from_full_report(ping_report):
        relevant_line = select_ping_summary_line(ping_report)
        return unpack_summary_line(relevant_line)
        
def unpack_summary_line(the_line):
        return int(the_line.split()[0]), int(the_line.split()[3]), float(the_line.split()[6].strip('%'))

def select_ping_summary_line(ping_report):
        split_report = ping_report.split('\n')
        relevant_line = [u for u in split_report if 'packets transmitted' in u]
        return relevant_line[0]

def format_data_point(d_out, host, target, ping_summary):
        return d_out.strip('\n') + ' ' + host + ' ' + target + ' ' + str(ping_summary[0]) \
                + ' ' + str(ping_summary[1]) + ' ' + str(ping_summary[2]) + '\n'

def encode_host(hostname_out):
        if 'Giovannis-MacBook-Pro-619.local' in hostname_out:
                return 'gf_mac'
        elif  'Giovannis-MacBook-Pro-619.local' in hostname_out:
                return 'ad_mac'
        else:
                return 'unkn'

import subprocess        
def get_host():
        hostname = subprocess.Popen(
	    ["hostname",],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	p_out, p_error = hostname.communicate()
        return encode_host(p_out)
        
