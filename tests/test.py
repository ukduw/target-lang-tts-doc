import pytest

from scrape import ScrapeText
from selective_translate import SelectiveTranslate
from tts import TextToSpeech


@pytest.mark.scrape
def test_seed():
    assert True # placeholder


@pytest.mark.translate
def test_translate():
    assert True # placeholder


@pytest.mark.tts
def test_tts():
    assert True # placeholder


# call: pytest -m scrape