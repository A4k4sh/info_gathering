import whois
import dns.resolver
import shodan
import socket
import requests
import argparse

argparse = argparse.ArgumentParser(description="This is a basic information gethering tool.", usage="python3 info_gethering.py -d Domain [-s IP]")
argparse.add_argument("-d", "--domain", help="Enter the domain name footprinting.")#,required=True
argparse.add_argument("-s","--shodan",help="Enter the IP for shodan search")
argparse.add_argument("-o","--output",help="Enter the file to write output to.")

args = argparse.parse_args()
domain = args.domain
ip = args.shodan
output = args.output

print("[+] Domain {} and IP {}".format(domain,ip))

#whois Module
print("[+] Getting whois info....")
whois_result = ''
#using whois libraray ,creating instance

try:
    py = whois.whois(domain)
    print("[+] whois info found.")
    whois_result += "Name:{}".format(py.domain_name) +'\n'
    whois_result += "Registrar: {}".format(py.registrar) +'\n'
    whois_result += "whois server: {}".format(py.whois_server) +'\n'
    whois_result += "Creation date: {}".format(py.creation_date) +'\n'
    whois_result += "Expiration date: {}".format(py.expiration_date) +'\n'
    whois_result += "Sever name: {}".format(py.name_servers) +'\n'
    whois_result += "country: {}".format(py.country) +'\n'
    whois_result += "updated data:{}".format(py.updated_date) +'\n'

except:
    pass
print(whois_result)

#dns Module
print("[+] Getting dns info.....")
dns_result = ''
#implementing dns.resolver from dnspython
try:
    for a in dns.resolver.resolve(domain,'A'):
        dns_result +="[+] A Record {}".format(a.to_text) + '\n'
    for ns in dns.resolver.resolve(domain,'NS'):
        dns_result +="[+] NS Record {}".format(ns.to_text) + '\n'
    for mx in dns.resolver.resolve(domain,'MX'):
        dns_result +="[+] MX Record {}".format(mx.to_text) + '\n'
    for txt in dns.resolver.resolve(domain,'TXT'):
        dns_result +="[+] txt Record {}".format(txt.to_text) + '\n'
except:
    pass
print(dns_result)

#Geolocation module
print("[+] Getting Geolocation info...")
geo_result =''
#implementing requests for web requests
try:
    response = requests.request('GET',"http://geolocation-db.com/json/"+socket.gethostbyname(domain)).json()
    geo_result +="[+] country_name: {}".format(response['country_code']) +'\n'
    geo_result +="[+] latitude:{}".format(response['latitude']) +'\n'
    geo_result +="[+] longitude: {}".format(response['longitude']) +'\n'
    geo_result +="[+] city: {}".format(response['city']) +'\n'
    geo_result +="[+] state: {}".format(response['state']) +'\n'
except:
    pass
print(geo_result)
#shodan Module
shodan_result =''
print("[+] Getting info from shodan for IP {}".format(ip))
if ip:
    #shodan api
    api = shodan.Shodan("uNglSaXod6xR4Ac7HatL8Yxoke5aR9Rs")
    try:
        results = api.search(ip)
        print("[+] Result found:{}".format(results['total']))

        for result in results ['matches']:
            shodan_result +="[+] IP :{} ".format(result['ip_str']) +'\n'
            shodan_result +="[+] data :\n {}".format(result['data']) +'\n'
            print()
            print(shodan_result)
    except:
        shodan_result +="[-] shodan search errror" +'\n'


if (output):
    with open(output, 'w') as file:
        file.write(whois_result +'\n\n')
        file.write(dns_result +'\n\n')
        file.write(geo_result +'\n\n')
        file.write(shodan_result +'\n\n')
