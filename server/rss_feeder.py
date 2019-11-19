import feedparser
import datetime

# feed = feedparser.parse(rss_url)
# feed_entries = feed.entries
# get current year and parse rss by the year (so I don't send all data to the frontend)
current_year = datetime.datetime.now().strftime('%Y')

def feedParser(link):
    rss_feed_dict = []

    feed = feedparser.parse(link)
    feed_entries = feed.entries

    for entry in feed_entries:
        if entry.has_key('published'):
            article_year = entry.published[12:16]
            if article_year == current_year: # compare published year with the current year and get only enties from current year
                data = {'title':entry.title, 'link': entry.links[0]['href'], 'published': entry.published}
                rss_feed_dict.append(data)
        else:
            data = {'title':entry.title, 'link': entry.links[0]['href'], 'category':entry.category}
            rss_feed_dict.append(data)
    return rss_feed_dict