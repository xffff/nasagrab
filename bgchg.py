from BeautifulSoup import BeautifulSoup
from appscript import *
import urllib2, urllib, sys, re, urlparse, os, datetime

# get image
def parsetags(url, path):
    u = urllib2.urlopen(url)
    soup = BeautifulSoup(u)
    for i in soup.findAll('a', attrs={'href': re.compile('(?i)(jpg|png)$')}):
        imgurl = urlparse.urljoin(url, i['href'])
        filename = i['href'].split("/")[-1]
        grabimg(imgurl, path, filename)

def grabimg(imgurl, path, filename):
    if not os.path.isfile(path + filename):
        print "Downloading: ", imgurl
        urllib.urlretrieve(imgurl, path + filename)
        print "Done!"
        bgchg(path + filename)
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
    now = datetime.datetime.now()
    apod = "http://apod.nasa.gov/apod/"
    modis = "http://modis.gsfc.nasa.gov/gallery/images/image{0}{1}{2}_500m.jpg".format(now.month,
                                                                                       now.day,
                                                                                       now.year)
    imgpath = "/Nasa/"
    grabimg(modis, imgpath, modis.split("/")[-1])
    parsetags(apod,imgpath)
    return 0

if __name__ == "__main__":
    sys.exit(main())
