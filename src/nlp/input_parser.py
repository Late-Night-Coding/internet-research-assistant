################# I M P O R T S #################
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
import spacy

stopWords = set(stopwords.words('english'))


class Input_Parser:

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

        print(self.tokens)

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
            if word not in stopWords:
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
        wordTokens = nltk.word_tokenize(sentence)
        for i in range(len(wordTokens)):
            wordTokens[i] = re.sub(r'[\W_]+', '', wordTokens[i]).lower()
        return wordTokens

    #############################################################################################################
    #  * Function:            __tokenize
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/09/2023
    #  *
    #  * Description:
    #  * Tokenize the sentences and remove everything that isn't a word
    #############################################################################################################
    def parse(self, sentence):
        # sentences = nltk.sent_tokenize(sent)
        sentences_tokens = self.__tokenize(sentence)
        sentences_tokens = self.__remove_stop_words(sentences_tokens)
        sentences_tokens = self.__lemmatize(sentences_tokens)
        sentence_tags = nltk.pos_tag(sentences_tokens)

        fdis = nltk.probability.FreqDist(sentences_tokens)
        print(fdis.most_common(5))
        return sentences_tokens, sentence_tags


if __name__ == "__main__":
    sent_short = "what are the rules of baseball "
    sent_long = "Experiments have been carried out for single crystalline silicon panels. Results are discussed and the increase in efficiency is investigated and understood. Operating problems are analyzed and the advantages of using underwater solar panels are pointed out."

    sent = sent_short
    main = Input_Parser(sent)
