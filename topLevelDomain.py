from tld import get_tld
# this funtion returns you the top level domain of a url.
def getTopLevelDomain(url):
    tld_url = get_tld(url,fix_protocol=True)
    return tld_url