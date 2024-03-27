from keybert import KeyBERT

class Extractor:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.model = KeyBERT()

    def keywords_extract(self, top_n: int = 5)-> list:
        keywords = self.model.extract_keywords(
            self.sentence,
            keyphrase_ngram_range=(1,1),
            stop_words='english',
            top_n=top_n,
            use_mmr=True,
            diversity=0.7
        )

        return keywords