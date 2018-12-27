# So we post advocates online, but sometimes they leave the company
# this should look up the advocates and see if they're still
# in the company LDAP.

# Maybe one day integrate this into a daily cron job that goes into
# wrike and actually removes the profile and webpage, but for now
# this was an exercise in using BeautifulSoup and pyldap just for
# my own benefit.

import urllib.request as urllib2
from bs4 import BeautifulSoup
import html2text
import ldap

ldap_uri = 'ldap://bluepages.ibm.com'
page = urllib2.urlopen('https://developer.ibm.com/profiles/')
soup = BeautifulSoup(page, 'html.parser')

print("Listing advocates...")

# find top buttons
advocates = []
advocate_h3s = soup.findAll('h3')
for advocate_h3 in advocate_h3s:
    advocates.append(advocate_h3.text)
    print(advocate_h3.text)

print("Looking up advocates...")

con = ldap.initialize(ldap_uri)
ldap_base = 'ou=bluepages,o=ibm.com'

no_entries = []
for advocate_name in advocates:
    # NOTE: Search by email or full name (cn)
    #query = "(email=" + advocate_email + ")"
    query = "(cn=" + advocate_name + ")"

    try:
        result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
        # The user was deleted from the LDAP if no result
        if not result:
            no_entries.append(advocate_name)
    except:
        print("ERROR: could not find " + advocate_name)

print(no_entries)
