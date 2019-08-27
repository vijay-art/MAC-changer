#!/usr/bin/env python

import subprocess
import re


interface = raw_input("enter your interface > ")
new_mac = raw_input("enter new mac address > ")



print("[+] your MAC address is chaging by RAHI to " + new_mac + "address")

subprocess.call(["ifconfig" , interface,"down"])
subprocess.call(["ifconfig" , interface,"hw", "ether", new_mac])
subprocess.call (["ifconfig" , interface,"up"])
  

output = subprocess.check_output("ifconfig " + interface ,shell = True)

print(output)

final_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output,)
print(final_result.group(0))
