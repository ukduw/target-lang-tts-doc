placeholder

notes:
-goal is to make consumption of a large quantity of text-heavy reports less time consuming and more approachable
-while helping user learn basics + technical jargon of their field in a foreign language

-script scrapes a number of institutional investor sites for Market Insights reports
    -this can be substituted for reports/papers of any field
-a dictionary of most common words is then used to machine translate a number of least common words (most likely to be technical jargon), depending on the total length, in the format:
    -foreign target language (original text)
-short, simple sentences are also translated to reinforce the basics of the target language

-this partially translated text is then converted to a short podcast with ElevenLabs API
-via bilingual ai voice map and text-to-speech engine