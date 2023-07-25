import argparse
import scapy.all as scapy
import sys
import os
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range. Example: 192.168.120.1/24")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target, use --help for more info.")
        
    return options

def clear_screen():
    os_name = os.name
    if os_name == "posix":  # Unix-based system (macOS, Linux, etc.)
        os.system("clear")
    elif os_name == "nt":   # Windows
        os.system("cls")
    else:
        print("Clear screen not supported for this operating system.")

clear_screen()

def scanip(ip):
      req_arp = scapy.ARP(pdst=ip)
      destination=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
      arp_req_des = destination/req_arp
      ans = scapy.srp(arp_req_des,timeout=1,verbose=False)[0]
      clear_screen()
      print(f"Enter the IP address of the network you want to scan: {ip}\n    `")
      print("This is a simple ARP scanner that scans the network for all the devices connected to it.\n")
      print(f"Total number of devices connected to the network are: {len(ans)}")
      print("--------------------------------------------")
      print("|\tIP\t    \t   MAC Address\t   |")
      print("--------------------------------------------")
      clinet_ips = []
      for j in ans:
            clinet_dic={"ip":j[1].psrc,"MAC":j[1].hwsrc}
            clinet_ips.append(clinet_dic)
            print(f"|  {j[1].psrc}   \t{j[1].hwsrc}  |")
      print("--------------------------------------------")
if os.geteuid() != 0:        
        print("Error: This script requires administrative/root privileges to perform ARP scanning.")
        print("Please run the script with 'sudo' or as an administrator.")
        sys.exit(1)
else :
    ip=get_arguments().target
    scanip(ip)
    print("\n")