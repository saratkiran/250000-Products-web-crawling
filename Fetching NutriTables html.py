import sys # Used to add the BeautifulSoup folder the import path
import urllib2 # Used to read the html document
import cookielib
import urllib
import simplejson
if __name__ == "__main__":
    ### Import Beautiful Soup
    ### Here, I have the BeautifulSoup folder in the level of this Python script
    ### So I need to tell Python where to look.
    sys.path.append("./BeautifulSoup")
    from bs4 import BeautifulSoup

    ### Create opener with Google-friendly user agent
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    domain_to_filter = 'www.google.com'    
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    ### Open page & generate soup
    ### the start" variable will be used to iterate through 10 pages.
   # for start in range(0,10):
    #    url = "http://www.google.com/search?q=site:stackoverflow.com&start"
    barcode = raw_input('Enter a barcode: ')
    barcode2 = 'site:directionsforme.org ' + barcode
    print barcode2
    query = urllib.urlencode({'q' : barcode2})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&start=50' \
    % (query)
    search_results = urllib.urlopen(url)
    json = simplejson.loads(search_results.read())
    results = json['responseData']['results']
    for i in results:
          resulturl = i['url']
          resulttitle = i['title']
#	  print i['title'] + ": " + i['url']
#          resulturl = i['url']

    print resulturl
    print resulttitle[:-17]

#    url = "http://www.directionsforme.org/index.php/directions/product/CEREALPL/00011110853530"	     
    req = req = urllib2.Request(resulturl, headers=hdr)
    page = urllib2.urlopen(req)
    page2 = page.read()
    page.close()
    soup = BeautifulSoup(page2)
 
    alltables = soup.findAll("table")
    results = []
    for table in alltables:
	rows = table.findAll('tr')
	lines = []
	for tr in rows:
		cols = tr.findAll('td')
		for td in cols:
			text = td.renderContents().strip('\n')
			lines.append(text)
	text_table = '\n'.join(lines)
	results.append(text_table)
    for result in results:
	with open(barcode+".txt", "w") as text_file:
		text_file.write("{}".format(result))

import datetime, xmlrpclib
wp_url = "http://www.arahant.in/wordpress/xmlrpc.php"
wp_username = "admin"
wp_password = "sarat18"
wp_blogid = ""
status_draft = 0
status_published = 1

server = xmlrpclib.ServerProxy(wp_url)

inputFn = "/home/saratkiran/Desktop/web/" + barcode + ".txt"
title = resulttitle[:-17] + barcode

try:
     with open(inputFn) as inputFileHandle:
            content = inputFileHandle.read()
except IOError:
     sys.stderr.write( "[myScript] - Error: Could not open %s\n" % (inputFn) )
     sys.exit(-1)
#content = "Body with lots of content"
#date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2011-10-20 21:08", "%Y-%m-%d %H:%M"))
categories = ["category here"]
tags = ["sometag", "othertag"] 
data = {'title': title, 'description': content, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)

###### this works
#    t = [x for x in soup.findAll('td')]
#    print [x.renderContents().strip('\n') for x in t]   
########
#    table = soup.findAll("table")

#    for row in table.find("tr"):
#	for cell in row.find("td"):
#		print cell.find('td' , { 'id': 'nutrition'})

	#print soup
   # anchor = [td.find("nutrition") for td in soup.findAll('td')]
    #print anchor
   # print soup.findAll("table")
    
        ### Parse and find
        ### Looks like google contains URLs in <cite> tags.
        ### So for each cite tag on each page (10), print its contents (url)
##    for cite in soup.findAll('title'):
  ##  	print cite.text

