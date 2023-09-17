from transformers import pipeline

class NLPProcessor:
    def __init__(self, model_name):
        self.nlp = pipeline("ner", model=model_name, tokenizer=model_name)

    def extract_entities(self, text):
        entities = self.nlp(text)
        return entities

    # You can add more NLP-related functions here as needed
