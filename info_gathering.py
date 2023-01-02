import whois
import dns.resolver
import shodan
import requests
import argparse

argparse = argparse.ArgumentParser(description="This is a basic information gathering tool." , usage="python3 info_gathring.py -d DOMAIN [-s IP]")
argparse.add_argument("-d","--domain",help="Enter the domain name footprinting.")
argparse.add_argument("-s","--shodan",help="Enter the IP for shodan search.")

args = argparse.parse_args()
domain=args.domain
ip=args.shodan

print("[+] Domain {} and  IP {}".format(domain,ip))

#whois module 
print("[+] Getting whois info....")

#using whois libaray,creating intance
try:
    py = whois.query(domain)
    print("Name: {}".format(py.name))
    print("Registrar: {}".format(py.registrar))
    print("Creation Date: {}".format(py.creation_date))
    print("Expiration Date: {}".format(py.expiration_date))
    print("Registrant: {}".format(py.registrant))
    print("Registrant Country: {}".format(py.registrant_country))
except:
        pass

