import feedparser
import httpx
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}


def get_feed(url) -> list:
    urls = (
        url,
    )

    # get the RSS feeds from feedparser
    feeds = [feedparser.parse(url) for url in urls]
    all_entries = [feed.entries for feed in feeds]

    return all_entries


def get_soup(url):
    re = httpx.get(url, headers=headers)
    soup = BeautifulSoup(re.content, 'lxml')
    if re.status_code == 404:
        return None
    else:
        return soup
