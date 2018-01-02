
import time       #Importing the time library to check the time of code execution
import sys    #Importing the System Library
import os
import re

known_indices = [11535266]
downloaded_indices = []

#Downloading entire Web Document (Raw Page Content)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

from bs4 import BeautifulSoup

char_link_re = re.compile("/lodestone/character/[0-9]*/")
while len(known_indices) > 0:
    # Load the entire page to get searchable text
    try:
        index = known_indices.pop(0)
        print("Processing %d" % index)
        url = "http://na.finalfantasyxiv.com/lodestone/character/%d/" % index
        page = download_page(url)
        soup = BeautifulSoup(page, 'html.parser')
        with open("page.html", 'w') as f:
            f.write(page)
        
        # Get this character portrait
        im_div = soup.find("div", class_=["frame__chara__face"])
        if im_div is not None:
            im_url = im_div.find("img").get("src")
            data = download_page(im_url)
            out_name = "%d.jpg" % index
            out_file = open(out_name, 'wb')
            out_file.write(data)
            out_file.close()
        downloaded_indices.append(index)

        # Find links to other character portraits

        for link in soup.find_all('a'):
            link_href = link.get('href')
            if char_link_re.match(link_href):
                new_ind = int(link_href.split("/")[3])
                if (not new_ind in downloaded_indices) and \
                   (not new_ind in known_indices):
                    known_indices.append(new_ind)








    except Exception as e:
        print("Exception for index %d: " % index, e)
