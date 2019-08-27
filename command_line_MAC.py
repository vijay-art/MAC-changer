#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change your device MAC_address")
parser.add_option("-m", "--MAC" , dest="new_mac" , help="for new mac address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] your MAC address is chaging by RAHI to " + new_mac + "address")

subprocess.call(["ifconfig" , interface,"down"])
subprocess.call(["ifconfig" , interface,"hw", "ether", new_mac])
subprocess.call (["ifconfig" , interface,"up"])

