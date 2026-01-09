from bs4 import BeautifulSoup
import json

# two types:
    # 2 very straightforward, all html/html-heavy with easy-to-use/clear categorization + clear schedule
    # other 2 way more complicated, with more pdfs/charts/videos, all kinds of html structures, category problems + no clear schedule

# LEAST to MOST complicated sources (2 easy, 2 hard...):
# 1) Deloitte - Weekly global economic update
    # 1/week, weds, all html
    # most straightforward and consistent by far
    # https://www.deloitte.com/us/en/insights/topics/economy/global-economic-outlook/weekly-update.html

# 3) JP Morgan - Market Insights
    # no clear schedule, all kinds of different html structures, pdfs, and charts...
    # they are categorized, but not via subtitle/tag - category is in each article address though, so can be filtered by links in html
    # https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/
# 4) BlackRock - Market Insights
    # no clear schedule, tons of different html structures, pdfs, tons of charts, videos (with transcripts, to be fair), etc. etc...
    # way too many categories
        # this may not be a downside - could select for a small handful of categories, eliminating most of the difficulties
    # https://www.blackrock.com/us/individual/insights

# ?) ...substacks?


deloitte_url = "https://www.deloitte.com/us/en/insights/topics/economy/global-economic-outlook/weekly-update.html"
example_url = "https://www.deloitte.com/us/en/insights/topics/economy/asia-pacific/japan-economic-outlook.html"
    # or navigate from root? don't know if same url is reused/updated

jpmorgan_url = "https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/"
blackrock_url = "https://www.blackrock.com/us/individual/insights"


class ScrapeText:

    def seed_check(self):
        LAST_ARTICLE_FILE = "last-article.json"
        with open(LAST_ARTICLE_FILE, "r") as f:
            last_article = json.load(f) # e.g. { "source1": "article_name", ... }

        del_la = last_article.get("deloitte")
        jpm_la = last_article.get("jpmorgan")
        br_la = last_article.get("blackrock")

        ScrapeText.scrape_deloitte(deloitte_url, del_la)
        ScrapeText.scrape_jpmorgan(jpmorgan_url, jpm_la)
        ScrapeText.scrape_blackrock(blackrock_url, br_la)

        # alter last_article dict
            # e.g. return last_article strings from below funcs...
        # json.dump the whole thing, overwriting previous
        with open(LAST_ARTICLE_FILE, "w") as f:
            json.dump(last_article, f, indent=2)

        return # needs to return list of strings of article text
    

    # these funcs need to take string param of last article
    # iterate through titles until that string is reached; only scrape ones before it
        # build list of article pages to be scraped
        # iterate through...
    # return string of name of the most recent article (first in list)
    def scrape_deloitte(self, source, la):
        del_soup = BeautifulSoup(source, 'html.parser')

        if la is None:
            # scrape first 5?
            return # list, [most recent title string, article text]
        else:
            # iterate over titles until la matches
            # append urls to list
            # scrape them for article text
                # needs logic to deal with titles, ignore figures and captions...
            return # list, [most recent title string, article text]

    def scrape_jpmorgan(self, source, la):
        jpm_soup = BeautifulSoup(source, 'html.parser')

        if la is None:
            # scrape first 5?
            return # list, [most recent title string, article text]
        else:
            # iterate over titles until la matches
            # append urls to list
            # scrape them for article text
                # needs logic to deal with titles, ignore figures and captions...
            return # list, [most recent title string, article text]

    def scrape_blackrock(self, source, la):
        br_soup = BeautifulSoup(source, 'html.parser')

        if la is None:
            # scrape first 5?
            return # list, [most recent title string, article text]
        else:
            # iterate over titles until la matches
            # append urls to list
            # scrape them for article text
                # needs logic to deal with titles, ignore figures and captions...
            return # list, [most recent title string, article text]
        
        