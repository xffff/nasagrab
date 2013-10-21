from BeautifulSoup import BeautifulSoup
import argparse, urllib2, urllib, sys, re, urlparse, os

def grabimg(url, imgpath):
    u = urllib2.urlopen(url)
    soup = BeautifulSoup(u)
    for i in soup.findAll('img', attrs={'src': re.compile('(?i)(jpg|png)$')}):
        imgurl = urlparse.urljoin(url, i['src'])
        name = i['src'].split("/")[-1]
        if not os.path.isfile(imgpath + name):
            urllib.urlretrieve(imgurl, imgpath + name)
            print "Downloading: ", imgurl
        else:
            print "Image ", name, " already exists"

def main():
    url = "http://apod.nasa.gov/apod/"
    imgpath = "/Nasa/"
    grabimg(url,imgpath)
    return 0

if __name__ == "__main__":
    sys.exit(main())
