import requests as r
import threading
import time
import argparse
import sys
import os

red = '\033[91m'
green = '\033[32m'
reset = '\033[0m'
purple = '\033[95m'
blue = '\033[34m'
yellow = '\033[93m'

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

banner = f"""
{red}     _____    _   _  __   __
    |  __ \  | \ | | \ \ / /
{green}    | |  | | |  \| |  \ V / 
{blue}    | |  | | | . ` |   > <  
 {yellow}   | |__| | | |\  |  / . \ 
 {purple}   |_____/  |_| \_| /_/ \_\   {green}v1.0

{reset}DNX Subdomain Finder
{yellow}Author: XTOM  
{blue}Usage: python DnX.py -d example.com -w wordlist.txt -t 100{reset}
"""
print(banner)

dns = argparse.ArgumentParser(description="Subdomain Finder")
dns.add_argument("-d", "--domain", required=True, help="Target domain")
dns.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
dns.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
dns.add_argument("-o", "--output", help="Output file to save results" ,default="subdomains.txt")
args = dns.parse_args()
domain = args.domain
wordlist = args.wordlist
num_threads = args.threads
dns_list = []
if not os.path.isfile(wordlist):
    print(f"Wordlist file '{wordlist}' not found!")
    sys.exit(1)

def enum(subdomains, results, lock):
    while True:
        lock.acquire()
        if not subdomains:
            lock.release()
            break
        sub = subdomains.pop()
        lock.release()
        url = f"http://{sub}.{domain}"
        try:
            response = r.get(url, timeout=3)
            if response.status_code == 200:
                lock.acquire()
                results.append(url)
                lock.release()
                print(f"{green}[+] Found: {url}")
                dns_list.append(url)
                with open(args.output, 'a') as out_file:
                    out_file.write(url + '\n')
        except r.RequestException:
            pass

def main():
    with open(wordlist, 'r') as f:
        subdomains = f.read().splitlines()
    results = []
    lock = threading.Lock()
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=enum, args=(subdomains, results, lock))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("\n[+] Enumeration complete.")
    print(f"[+] Found {len(results)} subdomains.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        sys.exit(0)
