from bs4 import BeautifulSoup
import urllib2, urllib, sys, re, urlparse, os, datetime, ctypes, random

# get image
def parsetags(opener, url, path):
    response = opener.open(url)
    u = response.read()
    # urllib2.urlopen(url)
    response.close()
    soup = BeautifulSoup(u)
    for i in soup.findAll('a', attrs={'href': re.compile('(?i)(jpg|png)$')}):
        imgurl = urlparse.urljoin(url, i['href'])
        filename = i['href'].split("/")[-1]
        grabimg(opener, imgurl, path, filename)

def grabimg(opener, imgurl, path, filename):
    if not os.path.isfile(path + filename):
        print "Downloading: ", imgurl
        try:
            # urllib2.install_opener(opener)
            data = None
            response = opener.open(imgurl) # urllib2.urlopen(imgurl)
            data = response.read()
            response.close()
        except Exception,e:
            print "Connection error:", e
        if data != None:
            with open(path+filename,'wb') as f:
                try:
                    f.write(data)
                    f.close()
                except Exception, e:
                    print "File write error: ", e
            print "Done!"
            return path+filename
    else:
        print "Image", filename, " already exists"
        return None

# change background to new image (osx, doesn't work very well)
def bgchg(p):
    print "changing wallpaper"
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER,0,p)

def main():
    now = datetime.datetime.now()
    apod = "http://apod.nasa.gov/apod/"
    modis = "http://modis.gsfc.nasa.gov/gallery/images/image{0}{1}{2}_500m.jpg".format(str(now.month).zfill(2),
                                                                                       str(now.day).zfill(2),
                                                                                       now.year)
    imgpath = "C:\\Nasa\\"
    bgtemp = []
    proxy = urllib2.ProxyHandler({'http':'localhost:53128'}) # cntlm
    opener = urllib2.build_opener(proxy)
    bgtemp.append(grabimg(opener, modis, imgpath, modis.split("/")[-1])) #grab directly from modis    
    bgtemp.append(parsetags(opener, apod, imgpath)) #grabs any images from apod

    if len(bgtemp) == 2:
        bgchg(bgtemp[random.randint(0,1)])
    elif len(bgtemp) == 1:
        bgchg(bgtemp[0])
    else:
        print "Error: No files downloaded"
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
