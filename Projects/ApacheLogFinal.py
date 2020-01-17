import re
import sys

#Accesslog file path
line="G:\\PYTHON\\Dummy\\Projects\\access_log"

def extract_ip(line):
    return line.split()[0]

def increase_count(ip_dict, ip_addr):
    if ip_addr in ip_dict:
       ip_dict[ip_addr] += 1
    else:
       ip_dict[ip_addr] = 1

def read_ips(infilename):
    res_dict = {}
    log_file = file(infilename)
    for line in log_file:
        if line.isspace():
           continue
        ip_addr = extract_ip(line)
        increase_count(res_dict, ip_addr)
    return res_dict

def write_ips(outfilename, ip_dict):
    out_file = file(outfilename, "w")
    for ip_addr, count in ip_dict.iteritems():
        out_file.write("%5d\t%s\n" % (count, ip_addr))
    out_file.close()

def parse_cmd_line_args():
    if len(sys.argv)!=3:
       print("Usage: %s [infilename] [outfilename]" % sys.argv[0])
       sys.exit(1)
    return sys.argv[1], sys.argv[2]

def main():
    infilename, outfilename = parse_cmd_line_args()
    ip_dict = read_ips(infilename)
    write_ips(outfilename, ip_dict)

if __name__ == "__main__":
    main()
