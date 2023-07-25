README

# ARP Scanner

## Description
ARP Scanner is a Python script that performs an Address Resolution Protocol (ARP) scan to discover devices connected to a specified IP or IP range on a local network. The script utilizes the scapy library for network scanning and provides a simple command-line interface for easy usage.

## Prerequisites
- Python 3.x
- scapy library (install using `pip install scapy`) or (install using `pip install -r requirements.txt`)
- Root/Administrator privileges (required for ARP scanning)

## Usage
1. Clone the repository or download the `Network_Scanner.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `Network_Scanner.py` script.
4. Run the script with root/admin privileges using:
   ```
   sudo python Network_Scanner.py -t <target_ip_or_ip_range>
   ```
   Example: `sudo python Network_Scanner.py -t 192.168.1.0/24`
5. The script will perform the ARP scan and display a list of devices with their corresponding IP and MAC addresses.

## Note
- This script requires root/admin privileges to perform ARP scanning, as it sends ARP packets.
- The terminal will be cleared before displaying the scan results for better visibility.

## Disclaimer
This script is intended for educational and legitimate network administration purposes only. Unauthorized scanning or accessing devices without proper authorization is illegal and unethical. The author is not responsible for any misuse of this tool. Use it responsibly and at your own risk.
