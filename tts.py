from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv
import os

load_dotenv()
EL_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(EL_API_KEY)
    

class TextToSpeech:
    # different source = different voice model/language?

    # ElevenLabs multilingual model
    # TTS engine + bilingual AI voice maps
        # configs: pitch, speech, pauses, volume, etc...
        # note: API supports mp3 - wav only via web
    # API docs: https://elevenlabs.io/docs/api-reference/introduction
        # Text to speech: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input
        # Dubbing: https://elevenlabs.io/docs/api-reference/dubbing/list
            # To experiment with dubbing (also interested to see result when using low quality audio from the 90s):
            # https://www.youtube.com/watch?v=HnQ2Lk20n3U

    def ElevenLabsTTS(self):
        return
    
