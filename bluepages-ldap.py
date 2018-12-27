# fewest lines of code to get a single entity from our LDAP

import ldap

ldap_uri = 'ldap://bluepages.ibm.com'
ldap_base = 'ou=bluepages,o=ibm.com'
query = "(cn=" + "Steve Martinelli)"

con = ldap.initialize(ldap_uri)
result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
print(result)
