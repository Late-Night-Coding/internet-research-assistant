################# I M P O R T S #################
import nltk
import nltk.corpus
from nltk.stem.wordnet import WordNetLemmatizer
import re

stop_words = set(nltk.corpus.stopwords.words('english'))
MIN_WORD_LEN = 3
MAX_WORD_LEN = 20

class InputParser:

    #############################################################################################################
    #  * Function:            __init__
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        02/08/2023
    #  *
    #  * Description:
    #  * Main driver of the program. Calls all the other functions to accomplish the task assigned.
    #############################################################################################################
    def __init__(self, sentence=None):

        if sentence is not None:
            self.tokens, self.token_tags = self.parse(sentence)
        else:
            self.tokens = None
            self.token_tags = None

    #############################################################################################################
    #  * Function:            __remove_stop_words
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/09/2023
    #  *
    #  * Description:
    #  * Removes stop words from a list of words
    #############################################################################################################
    def __remove_stop_words(self, tokens):
        result = list()
        for word in tokens:
            if word not in stop_words and MIN_WORD_LEN <= len(word) <= MAX_WORD_LEN:
                result.append(word)
        return result

    #############################################################################################################
    #  * Function:            __lemmatize
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/09/2023
    #  *
    #  * Description:
    #  * Cut words down to the most basic form
    #############################################################################################################
    def __lemmatize(self, tokens):
        results = list()
        lem = WordNetLemmatizer()
        for word in tokens:
            results.append(lem.lemmatize(word))
        return results

    #############################################################################################################
    #  * Function:            __tokenize
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/09/2023
    #  *
    #  * Description:
    #  * Tokenize the sentences and remove everything that isn't a word
    #############################################################################################################
    def __tokenize(self, sentence):
        word_tokens = nltk.word_tokenize(sentence)
        for i in range(len(word_tokens)):
            word_tokens[i] = re.sub(r'[\W_]+', '', word_tokens[i]).lower()
        return word_tokens

    #############################################################################################################
    #  * Function:            parse
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/09/2023
    #  *
    #  * Description:
    #  * Tokenize the sentences and remove everything that isn't a word
    #############################################################################################################
    def parse(self, sentence):
        # sentences = nltk.sent_tokenize(sent)
        tokens = self.__tokenize(sentence)
        tokens = self.__remove_stop_words(tokens)
        tokens = self.__lemmatize(tokens)
        sentence_tags = nltk.pos_tag(tokens)
        return tokens, sentence_tags

if __name__ == "__main__":
    sent_short = "what is the capital of the United States?"
    sent_long = "Experiments have been carried out for single crystalline silicon panels. Results are discussed and the increase in efficiency is investigated and understood. Operating problems are analyzed and the advantages of using underwater solar panels are pointed out."

    sent = sent_short
    sentences_tokens, tags = InputParser().parse(sent_short)

    print(sentences_tokens)
    print(tags)
