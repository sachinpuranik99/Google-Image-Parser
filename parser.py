from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib2
import argparse
import sys


if len(sys.argv) < 2 or len(sys.argv) > 2:
	print "ERROR: Please provide one celebrity name at a time in double quotes as the first argument"
	sys.exit()
elif not isinstance(sys.argv[1], basestring):
	print "Please provide name in quotes as a string"
	sys.exit()
else:
	print 

	
searchterm = sys.argv[1] # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"

# Download the chromedriver and insert the path in the following line if you dont have it in your PYTHONPATH already.
browser = webdriver.Chrome()
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(400):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print "Total Count:", counter
    print "Succsessful Count:", succounter
    print "URL:",json.loads(x.get_attribute('innerHTML'))["ou"]

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        req = urllib2.Request(img, headers={'User-Agent': header})
        raw_img = urllib2.urlopen(req).read()
        if("jpg" == imgtype):
            File = open(os.path.join(searchterm ,str(counter) + "." + imgtype), "wb")
            File.write(raw_img)
            succounter = succounter + 1
            File.close()
            print imgtype, File
    except:
            print "can't get img"

print succounter, "pictures succesfully downloaded"
browser.close()
