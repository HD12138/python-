from utils import urlManager
import requests
from bs4 import BeautifulSoup
import re

url = "http://www.crazyant.net"
urls = urlManager.UrlManager()
urls.urladd(url)

with open("craw_all_pages.txt", "w", encoding="utf-8") as fout:
    while urls.hasNewUrl():
        curr_url = urls.urlget()
        try:
            r = requests.get(curr_url, timeout=3)
            r.raise_for_status()  # 检查 HTTP 状态码是否为 4xx/5xx
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {curr_url}: {e}")
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string if soup.title else "No Title"

        fout.write(f"{curr_url}\t{title}\n")
        fout.flush()

        print(f"success: {curr_url}, {title}")

        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href is None:
                continue
            pattern = r'^https?://www\.crazyant\.net/\d+\.html$'
            if re.match(pattern, href):
                urls.urladd(href)
