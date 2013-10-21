from BeautifulSoup import BeautifulSoup
from appscript import *
import urllib2, urllib, sys, re, urlparse, os

# get image
def grabimg(url, imgpath):
    u = urllib2.urlopen(url)
    soup = BeautifulSoup(u)
    for i in soup.findAll('a', attrs={'href': re.compile('(?i)(jpg|png)$')}):
        imgurl = urlparse.urljoin(url, i['href'])
        filename = i['href'].split("/")[-1]
        if not os.path.isfile(imgpath + filename):
            print "Downloading: ", imgurl
            urllib.urlretrieve(imgurl, imgpath + filename)
            print "Done!"
            bgchg(imgpath + filename)
        else:
            print "Image", filename, " already exists"

# change background to new image (doesn't work very well)
def bgchg(p):
    se = app('System Events')
    desktops = se.desktops.display_name.get()
    for d in desktops:
        desk = se.desktops[its.display_name == d]
        desk.picture.set(mactypes.File(p))

def main():
    url = "http://apod.nasa.gov/apod/"
    imgpath = "/Nasa/"
    grabimg(url,imgpath)    
    return 0

if __name__ == "__main__":
    sys.exit(main())
