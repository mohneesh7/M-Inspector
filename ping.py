import subprocess
# This returns the ping status of the website/url.
def getping(url):
    text = subprocess.Popen(["ping -c 8 "+url], stdout=subprocess.PIPE, stderr=None, shell=True)
    text1 = text.communicate()[0]
    return text1
