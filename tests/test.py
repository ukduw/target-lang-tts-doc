import pytest

from scrape import ScrapeText
from selective_translate import SelectiveTranslate
from tts import TextToSpeech


@pytest.mark.scrape
def test_seed():
    ScrapeText.seed_check()
    assert True # placeholder

@pytest.mark.scrape
def test_scrape_del():
    ScrapeText.scrape_deloitte()
    assert True # placeholder

@pytest.mark.scrape
def test_scrape_jpm():
    ScrapeText.scrape_jpmorgan()
    assert True # placeholder

@pytest.mark.scrape
def test_scrape_br():
    ScrapeText.scrape_blackrock()
    assert True # placeholder



@pytest.mark.translate
@pytest.mark.parameterize("full_article,result", [
    ("Example text without punctuation", ["Example", "text", "without", "punctuation"]),
    ("Punctuation, for example, this sentence!", ["Punctuation", "for", "example", "this", "sentence"]),
    ("It's misc.'punc' sentences(?) that *cause* !@#$%^&* problems...", ["It's", "misc", "punc", "sentences", "that", "cause", "problems"]),
        # remember, this func's purpose is to be used with dictionary_check, so only the words themselves matter
])
def test_word_breakup(full_article, result):
    words = SelectiveTranslate.word_breakup(full_article)
    assert words == result

@pytest.mark.translate
def test_sentence_breakup():
    full_article = "An example. This time made up of multiple sentences! Not necessarily ending with the same punctuation?"
    sentences = SelectiveTranslate.sentence_breakup(full_article)
    assert sentences == ["An example.", "This time made up of multiple sentences!", "Not necessarily ending with the same punctuation?"]

@pytest.mark.translate
def test_dictionary_check():
    # needs dictionary...
    # supply SelectiveTranslate.dictionary_check(params) a list of words with known frequency
    # check that only the least common are returned
    assert True

@pytest.mark.translate
def test_sentence_length_check():
    sentences = ["First sentence.", "The second sentence is longer.", "The third sentence is longer than both the first and second combined."]
    length_checked, sentences_to_translate = SelectiveTranslate.sentence_length_check(sentences)
    assert length_checked == ["First sentence.", "The second sentence is longer."] # only sentences <= 8 words should be returned
    assert sentences_to_translate == 1
        # e.g. func finds total number of sentences and average length of sentences
        # uses these to determine how many sentences to translate, rather than set number, it'll be dynamic per article
        # about 1/3? of the short sentences, which will be smaller proportion of total sentences

@pytest.mark.translate
def test_total_length_check():


@pytest.mark.translate
@pytest.mark.parameterize("test_phrases,end_lang,result", [
    ("Excuse me, ...", "", ""),
    ("", "", ""),
    ("", "", ""),
        # remember, this func's purpose is to be used with dictionary_check, so only the words themselves matter
])
def test_translate_replace_text(test_phrases, end_lang, result):
    translated = SelectiveTranslate.translate_replace_text(test_phrases, end_lang)
    assert translated == result



@pytest.mark.tts
def test_tts():
    assert True # placeholder


# call: pytest -m scrape/translate/tts