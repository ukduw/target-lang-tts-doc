from bs4 import BeautifulSoup
from easynmt import EasyNMT
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv
import os

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
        # needs way to check for new article(s), e.g. via date? or store title of last article in txt?
        # if new, append to list?
        # iterate through list and run corresponding scrape_source() function below

        # if txt is empty/has no corresponding last article, that means it hasn't been scraped before
            # scrape x number of articles to seed
        return
    
    def scrape_deloitte(self):
        del_soup = BeautifulSoup(self.deloitte_url, 'html.parser')


    def scrape_jpmorgan(self):
        jpm_soup = BeautifulSoup(self.jpmorgan_url, 'html.parser')


    def scrape_blackrock(self):
        br_soup = BeautifulSoup(self.blackrock_url, 'html.parser')


class SelectiveTranslate:
    
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
    
    def ElevenLabsTTS(self):
        return
    

if __name__ == "__main__":
    # placeholder
    ScrapeText.seed_check()
    # placeholder