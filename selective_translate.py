import translators as ts


class SelectiveTranslate:
    # iterate through seed_check return (list of strings of article texts)

    # python machine translation
    # deepl engine via translators library
        # very high translation quality with more natural speech than google translate
        # strong handling of grammar, nuance
        # google and baidu's strengths don't really apply here
    # call method: res = ts.deepl(string_to_translate, to_language='fr')

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
    
