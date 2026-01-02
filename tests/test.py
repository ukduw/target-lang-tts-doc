import pytest

from scrape import ScrapeText
from selective_translate import SelectiveTranslate
from tts import TextToSpeech


@pytest.mark.scrape
def test_seed():
    assert True # placeholder


@pytest.mark.translate
def test_word_breakup():
    assert True # placeholder

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