import nltk
import spacy

class Input_Parser:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        sent = "Gus Proto is a Python developer currently working for a London-based Fintech"
        doc = self.nlp(sent)

        sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj")]

        print(sub_toks)

    def split(self, userInput):
        pass


if __name__ == "__main__":
    main = Input_Parser()