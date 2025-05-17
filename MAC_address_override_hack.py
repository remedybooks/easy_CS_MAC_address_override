#!/user/bin/env python
#WARNING:Code can cause system issues if NOT run on a virtual workstation

import subprocess
import optparse
import re

def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface")
    parser.add_option("-m", "--mac", dest="mac_override")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("No valid interface entered")
    if not options.mac_override:
        parser.error("No valid MAC address entered")
    return options

def override_mac (interface, mac_override):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_override])
    subprocess.call(["ifconfig", interface, "up"])

def show_mac (interface):
    address_output = subprocess.check_output(["ifconfig", interface])
    final_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", address_output)
    if final_result:
        return final_result.group(0)
    else:
        print("Error in the code exists.")

options = get_inputs()
print_mac = show_mac(options.interface)
print("Current MAC address is " + str(print_mac))
override_mac(options.interface, options.mac_override)
print_mac = show_mac(options.interface)
print("New MAC address is " + str(print_mac))
