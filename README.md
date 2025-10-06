# DnX
Subdomain Finder -- Written in python language
# About 
This tool performs basic level of subdomain enumeration
on any website ...
<img width="620" height="400" alt="dnx" src="https://github.com/user-attachments/assets/786d8b62-5997-46d3-8474-ba5ee182a033" />


# Installation
  # Linux or Termux 
  ``` https://github.com/cyberxtom/DnX ```
  ``` cd DnX ```
  ``` pip install -r requirement.txt```
  If packages are not installing then try 
  ``` python -m venv venv ```
  ``` source venv/bin/activate ```
  ``` pip install -r requirement.txt```
# Usage 
Commands 
      -h, --help            show this help message and exit
  -d, --domain DOMAIN   Target domain
  -w, --wordlist WORDLIST
                        Path to wordlist
  -t, --threads THREADS
                        Number of threads
  -o, --output OUTPUT   Output file to save results

Example 
 ``` python DnX.py -d {example.com} -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -t 100 ```
