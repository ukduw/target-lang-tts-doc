import pytest

from scrape import ScrapeText
from selective_translate import SelectiveTranslate
from tts import TextToSpeech


@pytest.mark.scrape
def test_seed():
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

    assert True

@pytest.mark.translate
def test_dictionary_check():
    assert True

@pytest.mark.translate
def test_sentence_length_check():
    assert True

@pytest.mark.translate
def test_total_length_check():
    assert True

@pytest.mark.translate
def test_translate_replace_text():
    assert True

@pytest.mark.tts
def test_tts():
    assert True # placeholder


# call: pytest -m scrape/translate/tts