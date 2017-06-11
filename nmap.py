import subprocess
# this gives the nmap scan of the target url/website.
def getnmap(url):
    a = subprocess.Popen(["nmap -F "+url],stdout=subprocess.PIPE,shell=True)
    b = a.communicate()[0]
    return b


