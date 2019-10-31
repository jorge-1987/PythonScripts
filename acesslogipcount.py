#!/usr/bin/env python
import os
import sys

file_name = "access.log"

ip_counts = {}
with open(file_name) as logfile:
    _ = logfile.readlines()
    for line in _:
        if "200" in line.split():
            try:
                ip_counts[line.split()[0]] += 1
            except Exception:
                ip_counts[line.split()[0]] = 1

for ip in ip_counts:
    if ip_counts[ip] > 100:
    	print (str(ip) + " " + str(ip_counts[ip]))
