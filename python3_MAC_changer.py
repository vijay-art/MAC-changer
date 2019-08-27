#!/usr/bin/env python

import subprocess

interface = input("enter your interfae > ")
new_mac = input("enter new_mac address > ")

print("[+] your MAC address changing by RAHI to " + new_mac + " address")

subprocess.call("ifconfig " + interface + " down ",shell = True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell = True)
subprocess.call("ifconfig " + interface + " up" , shell = True)

