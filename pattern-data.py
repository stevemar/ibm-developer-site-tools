import urllib2
from bs4 import BeautifulSoup
import html2text

root = 'retrieve-client-insights-for-wealth-management-companies'

try:
    page = urllib2.urlopen('https://developer.ibm.com/code/patterns/' + root)
except urllib2.HTTPError:
    print("skipping " + root + " as it is not published yet")

soup = BeautifulSoup(page, 'html.parser')

# find title
title_div = soup.find('h2', attrs={'class' : 'ibm-h2 sc_page_head'})
title_text = title_div.find('span').text.strip()
print "------------TITLE------------------"
print title_text

# find subtitle
subtitle_div = soup.find('h1', attrs={'class' : 'ibm-h1 pn-text-white'})
subtitle_text = subtitle_div.text.strip()
print "-------------SUBTITLE--------------------"
print subtitle_text

# find top buttons
youtube_link = ''
github_link = ''
button_links = soup.findAll('a', attrs={'class' : 'ibm-btn-sec ibm-btn-white'})
print "------------CODE_AND_VIDEO------------------"
for button_link in button_links:
    link = button_link['href']
    if '?' in link:
        link = link.split('?')[0]
    if 'github' in link:
        github_link = link
    if 'youtube' in link:
        youtube_link = link
    print youtube_link
    print github_link

# find last modified date
# last_updated_date = soup.find('span', attrs={'id' : 'project_last_modified'})
# print last_updated_date

# find authors
authors = []
author_links = soup.findAll('a', attrs={'class' : 'pn-text-white'})
print "-----------AUTHORS----------------"
for author_link in author_links:
    print author_link.text

# find description and convert it to markdown
description = soup.find('div', attrs={'class' : 'sc_description_cont pn-pb40'})
print "------------DESCRIPTION-------------------"
print html2text.html2text(description.text.strip())

# find overview and convert it to markdown
description = soup.find('div', attrs={'class' : 'sc_overview_cont'})
print "------------OVERVIEW------------------"
print html2text.html2text(description.text.strip())

# find links
link_divs = soup.findAll('article', attrs={'class' : 'pn-list__item post type-post status-publish format-standard hentry'})
for link_div in link_divs:
    print "------------LINKS--------------------"
    link_title = link_div.find('h2', attrs={'class' : 'entry-title'}).text
    link_href = link_div.find('a')['href']
    link_description = link_div.find('div', attrs={'class' : 'exc-content'})
    print link_title
    print link_href
    if link_description: print link_description.text.strip()

# print components
component_links = soup.findAll('a', attrs={'class' : 'ibm-btn-sec ibm-btn-teal-40 journey_tag'})
print "-----------COMPONENTS---------------"
for component_link in component_links:
    print component_link.text

tech_links = soup.findAll('a', attrs={'class' : 'ibm-btn-pri ibm-btn-teal-40 journey_tag'})
print "-----------TECHNOLOGIES---------------"
for tech_link in tech_links:
    print tech_link.text
