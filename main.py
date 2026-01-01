from bs4 import BeautifulSoup
from easynmt import EasyNMT
    # very large file size; consider just using translators (or other) package
    # use google, deepl, baidu translation...
    # script relies on accessing internet resources anyway; no need to use local translation, like easynmt
        # translation may also be higher quality?
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv
import os
import json

model = EasyNMT('opus-mt')

load_dotenv()
EL_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(EL_API_KEY)

# 1
# ElevenLabs multilingual model
# TTS engine + bilingual AI voice maps
    # configs: pitch, speech, pauses, volume, etc...
    # note: API supports mp3 - wav only via web
# API docs: https://elevenlabs.io/docs/api-reference/introduction
    # Text to speech: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input
    # Dubbing: https://elevenlabs.io/docs/api-reference/dubbing/list
        # To experiment with dubbing (also interested to see result when using low quality audio from the 90s):
        # https://www.youtube.com/watch?v=HnQ2Lk20n3U

# 2
# python machine translation - EasyNMT?
# use dictionary of most common words; use inverse to identify specialist/technical language
    # sparsely translate, label as lang, put original in brackets
# translate (some) full sentences below a certain length (basic sentences)
# update: a lot of new syntax... bit unsure of how to do it without hard-coding...
    # maybe determine total number of words + short sentences to be translated by the total length of the report
    # use these totals to limit a list to a max length
    # populate list with strings - most uncommon vocab (determined via dictionary of most common words) + sentences below x length
    # iterate through the list, machine translating each and adding the translations to another list...
    # replace original with structure "translation (original text)"
        # ...how can the position of the original be identified???
        # maybe they can be replaced with a jibberish marker as they're added to list...

# 3
# would rather set up periodic scrape/checks
# two methods:
    # some are very straightforward, with weekly updates...
    # others do not seem to have a set schedule
        # may have to store the latest title as string
        # each scrape iterates through titles, stopping when it reaches the stored one
# two types:
    # 2 very straightforward, all html/html-heavy with easy-to-use/clear categorization + clear schedule
    # other 2 way more complicated, with more pdfs/charts/videos, all kinds of html structures, category problems + no clear schedule

# LEAST to MOST complicated sources (2 easy, 2 hard...):
# 1) Deloitte - Weekly global economic update
    # 1/week, weds, all html
    # most straightforward and consistent by far
    # https://www.deloitte.com/us/en/insights/topics/economy/global-economic-outlook/weekly-update/weekly-update-2025-06.html

# 3) JP Morgan - Market Insights
    # no clear schedule, all kinds of different html structures, pdfs, and charts...
    # they are categorized, but not via subtitle/tag - category is in each article address though, so can be filtered by links in html
    # https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/
# 4) BlackRock - Market Insights
    # no clear schedule, tons of different html structures, pdfs, tons of charts, videos (with transcripts, to be fair), etc. etc...
    # way too many categories
        # this may not be a downside - could select for a small handful of categories, eliminating most of the difficulties
    # https://www.blackrock.com/us/individual/insights


# ?) EPA?
    # https://onlinelibrary.wiley.com/journal/23806567

# ?) ...substacks?


# don't forget to pip freeze > requirements.txt after writing script...
# write readme
# export TMPDIR=/path/to/tmp/with/disk/space, /tmpdir

# how to select language/voice map? maybe cycle through or per source?



class ScrapeText:
    deloitte_url = "https://www.deloitte.com/us/en/insights/topics/economy/global-economic-outlook/weekly-update/weekly-update-2025-06.html"
    example_url = "https://www.deloitte.com/us/en/insights/topics/economy/asia-pacific/japan-economic-outlook.html"
        # or navigate from root? don't know if same url is reused/updated

    jpmorgan_url = "https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/"
    blackrock_url = "https://www.blackrock.com/us/individual/insights"

    def seed_check(self):
        LAST_ARTICLE_FILE = "last-article.json"
        with open(LAST_ARTICLE_FILE, "r") as f:
            last_article = json.load(f) # e.g. { "source1": "article_name", ... }

        # call scrape_x functions
        del_la = last_article.get("deloitte")
        jpm_la = last_article.get("jpmorgan")
        br_la = last_article.get("blackrock")

        ScrapeText.scrape_deloitte(del_la)
        ScrapeText.scrape_jpmorgan(jpm_la)
        ScrapeText.scrape_blackrock(br_la)

        # if all most_recent titles match, return early
            # does this need to be in if __name__...?
            # e.g. if this func returns empty list, return

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
    def scrape_deloitte(self, la):
        if la is None:
            return # placeholder, scrape first 5

        del_soup = BeautifulSoup(self.deloitte_url, 'html.parser')
        return # most recent title string

    def scrape_jpmorgan(self, la):
        if la is None:
            return # placeholder, scrape first 5

        jpm_soup = BeautifulSoup(self.jpmorgan_url, 'html.parser')
        return # most recent title string

    def scrape_blackrock(self, la):
        if la is None:
            return # placeholder, scrape first 5

        br_soup = BeautifulSoup(self.blackrock_url, 'html.parser')
        return # most recent title string


class SelectiveTranslate:
    # iterate through seed_check return (list of strings of article texts)

    def word_breakup(self):
        return

    def sentence_breakup(self):
        return

    def dictionary_check(self):
        return
    
    def sentence_length_check(self):
        return
    
    def total_length_check(self):
        return

    def translate_replace_text(self):
        return
    
    
class TextToSpeech:
    # different source = different voice model/language?

    def ElevenLabsTTS(self):
        return
    

if __name__ == "__main__":
    # placeholder
    ScrapeText.seed_check()
    # placeholder