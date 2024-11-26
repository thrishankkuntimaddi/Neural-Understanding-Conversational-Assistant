# nlp_processor.py
import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_intent(self, user_input):
        doc = self.nlp(user_input)
        if "remind" in user_input:
            return "reminder"
        return "general"

    def extract_entities(self, user_input):
        doc = self.nlp(user_input)
        return [(ent.text, ent.label_) for ent in doc.ents]
