from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
from nt import link
import crawl


class LinkParser(HTMLParser):

    def starttag(self, tag, attributes):
        if tag == 'a':
            for (key, value) in attributes:
                if key == 'href':
                    url_new = parse.urljoin(self.baseUrl, value)
                    self.links_list = self.links_list + [url_new]

   
    def getLinks(self, url):
        self.links_list = []
        self.baseUrl = url
        response = urlopen(url)
        htmlBytes = response.read()
        htmlString = htmlBytes.decode("utf-8")
        self.feed(htmlString)
        return self.links_list

def crawl(url,maxPages):  
    pagesToVisit = [url]
    pagesVisited = 0

    while pagesVisited < maxPages and pagesToVisit != []:
        pagesVisited = pagesVisited +1
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        parser = LinkParser()
        links = parser.getLinks(url) 
        pagesToVisit = pagesToVisit + links
       
    file=open("links.txt","w")
    file.write("\n".join(pagesToVisit))
    
crawl("https://en.wikipedia.org/wiki/Web_crawler", 100)