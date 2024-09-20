"""
PENROSE PORTSCAN NMAP PENETRATION TOOL 0.2.a

Streamlines usage of nmap slightly. More or less a coding project.
Not recommended to use in a professional setting.

Future updates(if I don't abandon this project) is further streamlining,
adding additional options and combining tools to create a more
optimal port scanner.

Ensure proper module installation before running
"""

from dep import *

print("""
Welcome to PENROSE PORTSCAN, penetration testing tool
=====================================================
This tool is not a professional program and only
utilizes the most basic forms of nmap, and is, at this point,
a proof of concept and streamlines the enumeration process. 
There are most certainly better programs that do the same 
thing and offer more features than this program, even with 
better evasion tactics.

This program is open source, does not collect any data, 
IP Addresses or information, and you may make changes
to this program at your leisure.

I kindly ask that you do not use this program maliciously.
I am not responsible for consequences following 
exploitations, if any, uncovered by this program.
=====================================================
PLEASE ENTER 'y' TO ACCEPT.
""")
agreement = input(line_at)

if agreement.lower() == 'y':
    os.system('clear')
    print(PENROSE)
else:
    exit(0)

# Vars
uinput = ""
command = ""
target = "No Target"

# Options
stype = " -O"
speed = " -T1 "
sport = ""
frag = ""
decoy = ""
pingflag = ""

while True:
    uinput = input(line_at)
    try:
        segmented = uinput.split(" ")
        command = segmented[0].lower()
        info = segmented[1].lower()
    except IndexError:
        info = ""

    if command == "quit":
        print("Exiting PENROSE")
        break
    elif command == "options":
        print(options + "\n")
    elif command == "clear":
        os.system("clear")
        print(PENROSE)
    elif command == "lip":
        print(f"Your IP => {get_ip()}")
    elif command == "rhost":
        target = info
        print(f"RHOST => {target}")
    elif command == "prtarget":
        if target == "":
            print("Please select a target with RHOST to use this command.")
        else:
            print(target)
    elif command == "ping":
        if target == "No Target":
            print("Please select a target with RHOST to use this command.")
        else:
            validate_ip_address(target)
    elif command == "setype":
        if info == "version":
            stype = " -sV"
        elif info == "os":
            stype = " -O"
        elif info == "ss":
            stype = " -sS"
        elif info == "st":
            stype = " -sT"
        elif info == "all":
            stype = " -A"
            sport = ""
        else:
            print("Unknown scan type, please refer to options menu.")
        print(f"Scantype => {info}")
        if info == "all":
            print(f"Ports => All")
    elif command == "sespeed":
        if info == "0":
            speed = " -T0 "
        elif info == "1":
            speed = " -T1 "
        elif info == "2":
            speed = " -T2 "
        elif info == "3":
            speed = " -T3 "
        elif info == "4":
            speed = " -T4 "
        elif info == "5":
            speed = " -T5 "
        else:
            print("Unknown speed type, please refer to options menu.")
        print(f"Speed => {info}")
    elif command == "seport":
        if info == "common":
            sport = ""
        elif info.find("-") or info.isdigit() :
            sport = "-p " + info + " "
        else:
            print("Could not determine ports, please refer to options menu.")
        if info == "common":
            print(f"Ports => common 1000 ports")
        else:
            print(f"Ports => {info}")
    elif command == "sefrag":
        if info == "t":
            frag = "-f "
            print("frag => True")
        else:
            frag = ""
            print("frag => False")
    elif command == "sedecoy":
        if info == "t":
            decoy = f"-D {get_decoy_ips(5, get_ip())} "
            print("decoy => True")
        else:
            decoy = ""
            print("decoy => False")
    elif command == "sepingflag":
        if info == "t":
            pingflag = "-Pn "
            print("Ping Flag => True")
        else:
            pingflag = ""
            print("Ping Flag => False")
    elif command == "prnmap":
        print_nmap(stype, speed, pingflag, decoy, frag, sport, target)
    elif command == "run":
        if target == "No Target" or target == "":
            print("Please select a target")
        else:
            run_nmap(stype, speed, pingflag, decoy, frag, sport, target)
    else:
        print("Unknown command, please refer to options menu.")

exit(0)
