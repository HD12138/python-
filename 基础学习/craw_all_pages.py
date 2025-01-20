from utils import urlManager
from utils import urlManager
import requests
from bs4 import BeautifulSoup
import re

url = "http://www.crazyant.net"
urls = urlManager.UrlManager();
urls.urladd(url)

fout = open("craw_all_pages.txt","w")
while urls.hasNewUrl():
    curr_url = urls.urlget()
    r = requests.get(curr_url,timeout=3)
    if r.status_code != 200:
        print("error-404")
        continue
    soup = BeautifulSoup(r.text,"html.parser")
    title = soup.title.string

    fout.write("%s\t%s\n"%(curr_url, title))
    fout.flush()

    print("success:%s, %s"%(curr_url,title))

    links = soup.find_all("a")
    for link in links:
        href = link["href"]
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern,href):
            urls.urladds(href)

fout.close()