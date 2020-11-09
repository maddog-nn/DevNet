#!/usr/bin/python3

import re
import subprocess as sp

# Open file with ip addresses
with open("/home/sd/Codding/Python/ip-to-dns/ip-addresses.txt") as f:
    result = f.readlines()

# Getting ip from file and trying to resolve ip to dns name
for line in result:
    ip_address = re.search(r'((\d+)\.){3}\d+', line).group()
    dns_name = sp.run(f'dig -x {ip_address} +short', shell=True, stdout=sp.PIPE, encoding='utf-8')
    if dns_name.stdout:
        # print(f'IP {ip_address} is {dns_name.stdout.strip()}')
        print(f'| {ip_address} | {dns_name.stdout.strip()} |')
    else:
        # print(f'IP address {ip_address} has no DNS record.')
        print(f'| {ip_address} | *Has no DNS record* |')