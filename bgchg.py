from BeautifulSoup import BeautifulSoup
import argparse, urllib2, sys, re, urlparse

def grabimg(url, imgpath):
    u = urllib2.urlopen(url)
    soup = BeautifulSoup(u)
    for i in soup.findAll('img', attrs={'src': re.compile('(?i)(jpg|png)$')}):
        imgurl = urlparse.urljoin(url, i['src'])
        urllib2.urlretrieve(imgurl, imgpath)
        print "Downloading: ", imgurl

def main():
    url = "http://apod.nasa.gov/apod/"
    imgpath = "/Nasa"
    grabimg(url)
    return 0

if __name__ == "__main__":
    sys.exit(main())
