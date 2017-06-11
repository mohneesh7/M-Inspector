import nmap
import ping
import topLevelDomain
import whois
import robots
import os

# integrates all the functions.
pname = raw_input("give project name :")
raw_ip = raw_input("enter The website to be scanned :")
tld_ip = topLevelDomain.getTopLevelDomain(raw_ip)
path = pname
if not os._exists(pname):
    os.makedirs(path)
pingdata = ping.getping(tld_ip)
nmapdata = nmap.getnmap(tld_ip)
whoisdata = whois.getwhois(tld_ip)
robotsdata = robots.getrobot(tld_ip)
fo = open(pname+'/ping.txt','w')
fo.write(pingdata)
fo.close()

fo = open(pname+'/whois.txt','w')
fo.write(whoisdata)
fo.close()

fo = open(pname+'/nmap.txt','w')
fo.write(nmapdata)
fo.close()

fo = open(pname+'/robots.txt','w',1)
fo.write(robotsdata)
fo.close()

