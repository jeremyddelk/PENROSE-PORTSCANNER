# Line @

line_at = "PENROSE:> "

# Modules

import os
import random
import socket
import struct
import subprocess
import time
from logging import exception

import requests

# STRING FORMATS

PENROSE = """
                         xç@@@@@@@@@@                         
                        xççç@@@@@@@@@ç                        
                       xççççç@@@@@@@@@ç                       
                      xççççççç@@@@@@@@@@                      
                     xççççççççç@@@@@@@@@@                     
                    xççççççççççç@@@@@@@@@ç                    
                   çççççççççççççç@@@@@@@@@@                   
                  xççççççççççççççç@@@@@@@@@@                  
                 xççççççççççççççççx@@@@@@@@@@                 
               ûçççççççççxxxçççççççç@@@@@@@@@@                
              xxççççççççxûûûççççççççç@@@@@@@@@@               
              xççççççççxûûûûûxçççççççç@@@@@@@@@@              
             çççççççççxûûûûûûûxççççççççç@@@@@@@@@             
           xçççççççççxûûûûûûûûûççççççççç@@@@@@@@@@ç           
           xççççççççxûûûûûûûûûûxxççççççççç@@@@@@@@@           
         xççççççççxxûûûûûûûûûû  xçççççççççç@@@@@@@@@          
        xçççççççççxûûûûûûûûûû    xxççççççççç@@@@@@@@@ç        
       xçççççççççxûûûûûûûûûû       xççççççççç@@@@@@@@@ç       
      xçççççççççxûûûûûûûûûû        xçççççççççç@@@@@@@@@x      
     xççççççççxxûûûûûûûûûû          xçççççççççç@@@@@@@@@ç     
    xçççççççççxûûûûûûûûûxççççççççççççxçççççççççç@@@@@@@@@ç    
   ûçççççççççxûûûûûûûûx@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ç   
  xççççççççxxûûûûûûûûx@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ç  
 xçççççççççxûûûûûûûûx@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
xççççççççxxûûûûûûûûx@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ç
xçççççççxxûûûûûûûûûxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 xççççççxûûûûûûûûûûûûûûûûû /PENROSE \\ûûûûûûûûûûûûûûûûûûûûûûûûû
  xçççxxûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûû 
   xççûûûûûûûûûûûûûûûûûûû/ PORT-SCAN \\ûûûûûûûûûûûûûûûûûûûûûûû  
    xxûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûûû 
                    enter options to begin
"""

options = """
PENROSE is not a professional program and is not recommended in a professional setting
==========================================================================
Available Commands:

quit = Exit program

clear = clears terminal, reprints penrose

lip = Display your local_ip address

rhost = RHOST <IP ADDRESS> sets the target IP
    Example: RHOST 192.168.38.2
    
prtarget = Print current target's IP

ping = Ping target after RHOST is set

prnmap = Preview your nmap command before execution

run = Runs the program
        !-DOUBLE CHECK SETTINGS

==========================================================================
Options:

setype all, version, os, ss, st = Sets type scan to all, version or os scan. OS is default

sespeed 0, 1, 2, 3, 4, 5 = Sets speed of the scan. 1 is default

seport common, <single port>, <start-range>-<end-range> = Sets ports to scan. Common ports are default

sefrag t, f = Sets decoy value true or false, breaks packages into fragments. Default to false

sedecoy t, f = Sets decoy value true or false, sends 5 decoy IP Addresses. Default to false

sepingflag t, f = Sets ping flag to true or false. Default to false

Please reference nmap guide if you do not know what these options are
More options, scan types, and features coming in the future
"""

# FUNCTIONS

def get_ip():
    get_info = 'https://ipinfo.io/json'
    response = requests.get(get_info, verify=True)

    if response.status_code != 200:
        exception("Error sending requests for IP info. Exiting")
        exit(-1)
    else:
        return response.json()['ip']

def print_nmap(stype, speed, pingflag, decoy, frag, sport, target):
    print(f"sudo nmap{stype}{speed}{sport}{pingflag}{frag}{decoy}{target}")

def run_nmap(stype, speed, pingflag, decoy, frag, sport, target):
    os.system(f"sudo nmap{stype}{speed}{sport}{pingflag}{frag}{decoy}{target}")

def get_decoy_ips(size, local_ip):
    # Remove device identifier
    random_ips = []
    x = size
    while x > 0:
        random_ips.append(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
        x-=1
    random_ips.append(f"ME {local_ip}")
    return ",".join(random_ips)

def validate_ip_address(ip):
    if ip == "":
        return False

    command = f"sudo -S nmap -sn {ip}"

    result = subprocess.check_output(command, shell=True, universal_newlines=True)
    if result:
        print(result)
        return True

    time.sleep(1)
    print("Host is invalid or decided not to respond to ping request\n")
    return False

def scan_ports():
    pass