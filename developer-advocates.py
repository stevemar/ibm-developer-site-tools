import urllib2
from bs4 import BeautifulSoup
import html2text

page = urllib2.urlopen('https://developer.ibm.com/profiles/)
soup = BeautifulSoup(page, 'html.parser')

# find top buttons
advocates = []
advocate_divs = soup.findAll('div', attrs={'class' : 'profile-picture__wrap'})
for advocate_div in advocate_divs:
    print advocate_div.text
    advocates.add(advocate_div.text)
