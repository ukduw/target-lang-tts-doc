from scrape import ScrapeText
from selective_translate import SelectiveTranslate
from tts import TextToSpeech


# don't forget to pip freeze > requirements.txt after writing script...
# write readme


if __name__ == "__main__":
    # placeholder
    article_text = ScrapeText.seed_check()
        # if all most_recent titles match, return early
        # e.g. if this func returns empty list, return
            # wouldn't work here
            # needs logic in subsequent funcs to return early if not article_text
    # placeholder

# set up periodic scrape/checks
# two types:
    # some are very straightforward, with weekly updates...
    # others do not seem to have a set schedule

