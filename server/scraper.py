import requests
import time
import random
import json
import os

from bs4 import BeautifulSoup
from urllib.request import urljoin, urlparse
from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation


def start_scraping():
    print('--- scraping started', time.asctime( time.localtime(time.time()) ))
    get_all_website_links(START_URLS)
    scraped_data = fetch_page(internal_urls)

    a = TorrDataPipeline(scraped_data)
    a.process_item(scraped_data)
    print('--- scraping ended', time.asctime( time.localtime(time.time()) ))

# ----------------- move to items.py -----------------
# ----------------- move to items.py END--------------


# ----------------- DATABASE -----------------
Base = declarative_base()

def db_connect():
    return create_engine('sqlite:///torr.db')

def create_data_table(engine):
    Base.metadata.create_all(engine)

class TorrData(Base):
    __tablename__ = 'torrData'

    id      = Column('id', Integer, primary_key=True)
    title   = Column('title', Text)
    mlink   = Column('mlink', Text)
    image   = Column('image', Text)
    date    = Column('date', Text)
    size    = Column('size', Text)

    # def __init__(self, id, title, mlink, image, date, size):
    #     self.id         = id
    #     self.title      = title
    #     self.mlink      = mlink
    #     self.image      = image
    #     self.date       = date
    #     self.size       = size
# ----------------- DATABASE END---------------

class TorrDataPipeline(object):

    def __init__(self, item):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        self.item = item
        engine = db_connect()
        create_data_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        for i in item:
            data = TorrData(title=i['title'],
                            mlink=i['magnet_l'],
                            image=i['image'],
                            date=i['date'],
                            size=i['size'])
            sth = session.query(TorrData).filter_by(title=i['title']).first()
            if sth is None:
                try:
                    session.add(data)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()
            else:
                session.close()
# ----------------- DB connection and processing END --------------


INPUT_DATA = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'input_data.json'))
with open(INPUT_DATA, 'r') as input_data:
    data = input_data.read()
obj = json.loads(data)

START_URLS = str(obj['INITIAL_URL'])
URL_PREFIX = str(obj['PREFIX_URL'])
# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

def is_valid(url):
    #Checks whether `url` is a valid URL.
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def bs_fetch(url):
    return BeautifulSoup(requests.get(url).content, "html.parser")

def get_all_website_links(url):
    urls = set() # all URLs of `url`
    domain_name = urlparse(url).netloc # domain name of the URL without the protocol
    soup = bs_fetch(url)
    for a_tag in soup.select('.gai td a:nth-of-type(3)'):
        href = a_tag['href']
        if href == '' or href is None: # href empty tag
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href): # not a valid URL
            continue
        if href in internal_urls: # already in the set
            continue
        if domain_name not in href: # external link
            if href not in external_urls:
                # print(f"[!]External link: {href}")
                external_urls.add(href)
            continue
        # print(f"[*] Internal link: {href}")
        urls.add(href)
        internal_urls.add(href)
    return urls

def fetch_page(url):
    scraped_data = []
    for follow_url in url:
        url_data = {}
        time.sleep(random.uniform(1.38, 2.27))
        soup = bs_fetch(follow_url)
        # get magent link, title and picture
        magnet_l = soup.select('div#download > a:nth-of-type(1)')[0]['href']
        title = soup.select('div#content > h1')[0].get_text()
        image = soup.find('table', id='details').find('img')['src']
        date = soup.find_all("td",{"class":"header"})[4].find_next_sibling('td').get_text().split('-')[0:2]
        date = '-'.join(date)
        size = soup.find_all("td",{"class":"header"})[5].find_next_sibling('td').get_text().split(" (")[0];

        url_data['title'] = title
        url_data['magnet_l'] = magnet_l
        url_data['image'] = image
        url_data['date'] = date
        url_data['size'] = size

        scraped_data.append(url_data)
    return scraped_data


if __name__ == "__main__":
    start_scraping()