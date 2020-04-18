def summary_from_full_report(ping_report):
        relevant_line = select_ping_summary_line(ping_report)
        return unpack_summary_line(relevant_line)
        
def unpack_summary_line(the_line):
        try:
                return int(the_line.split()[0]), int(the_line.split()[3]), float(the_line.split()[6].strip('%'))
        except ValueError:
                print('ValueError has occurred')
                print('the_line is: %s'%the_line)
                print('the_line was split like this: %s,   %s,  %s'%(the_line.split()[0],the_line.split()[3],the_line.split()[6].strip('%') ) )
        except:
                print('An exception has occurred (not ValueError)')
                print('the_line is: %s'%the_line)
                print('the_line was split like this: %s,   %s,  %s'%(the_line.split()[0],the_line.split()[3],the_line.split()[6].strip('%') ) )


def select_ping_summary_line(ping_report):
        split_report = ping_report.split('\n')
        relevant_line = [u for u in split_report if 'packets transmitted' in u]
        if len( relevant_line ):
                return relevant_line[0]
        else:
                print("\n** ISSUE in ping report (report format violation), which is: ")
                print(ping_report)
                print("\n** ISSUE in ping report, returning hard-coded line with negatice received (format violation)")
                return '10 packet tronsmitted, -1 packets received, 100.0% packet loss'
                
def format_data_point(d_out, host, target, ping_summary):
        return d_out.strip('\n') + ' ' + host + ' ' + target + ' ' + str(ping_summary[0]) \
                + ' ' + str(ping_summary[1]) + ' ' + str(ping_summary[2]) + '\n'



def encode_host(hostname_out):
        if    'Giovannis-MacBook-Pro-619.local' in hostname_out:
                return 'gfmac'
        elif  'Annes-MacBook-Pro.local' in hostname_out:
                return 'admac'
        elif  'ANNEs-MacBook-Pro-4.local' in hostname_out:
                return 'admaco'
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


def get_outout_path():
        '''returns target directory for writing files, based on  discovered host'''
        host     = get_host()
        if   host == 'gfmac':
                return '/Users/franzoni/Dropbox/Home/radio-tv/ping-tests/'
        elif host == 'admac' or host == 'admaco':
                return '/Users/dabrows/Dropbox/Home/radio-tv/ping-tests/'
        else:
                return './'

