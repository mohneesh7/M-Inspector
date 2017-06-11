import subprocess
# this returns whois information of the url/website.
def getwhois(url):
    p = subprocess.Popen(["whois "+url],stdout=subprocess.PIPE,shell=True)
    out = p.communicate()[0]
    return out
