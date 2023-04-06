import nltk
import asyncio
from collections import defaultdict
from nlp.input_parser import Input_Parser
from searches.openai_search import OpenAI
from searches.webpage_downloader import download_page

#############################################################################################################
#  * Function:            __basic_summarize__
#  * Author:              Blake
#  * Date Started:        03/28/2023

#  * Description:
#  * Returns a summary of the contents from a webpage.

#  * Parameters:
#  * content                str             contents from a webpage
#  * keywords               list[str]       list of keywords that will take priority when summarizing
#  * max_summary_length     int             max length of the summary to be returned
#############################################################################################################
def __basic_summarize__(content: str,
                    keywords: list[str]=[],
                    max_summary_length: str = 1000,
                    min_sent_len = 30,
                    max_sent_len = 250,
                    top_n_words = 50
                    ):
    """Given the text content of a webpage, return a summary of it that doesn't exceed max_summary_length characters.
    If keywords is not empty, sentences containing keywords will be more likely to be included"""

    input_parser = Input_Parser()

    # extract sentences
    sentences = nltk.sent_tokenize(content)

    # filter out sentences that are too big or too small
    sentences = [
        sentence for sentence in sentences
        if min_sent_len < len(sentence) < max_sent_len
    ]

    if len(sentences) == 0:
        return ""

    # find common words
    word_counter = nltk.probability.FreqDist((
        word
        for sentence in sentences
        for word in input_parser.parse(sentence)[0]
    ))

    # calculate word scores, in range [0, 1]
    maximum_frequency = word_counter.most_common(1)[0][1]
    word_scores = defaultdict(lambda: 0)
    for (top_word, word_freq) in word_counter.most_common(top_n_words):
        word_scores[top_word] = word_freq / maximum_frequency

    # calculate sentence scores, in range [0, inf)
    sentence_scores = [
        # sum over the word scores in the sentence to get its score
        sum((
            (word_scores[word] + (1 if word in keywords else 0))
            for word in set(input_parser.parse(sentence)[0])
        ))
        for sentence in sentences
    ]

    # TODO: Maybe we should make sentences nearby highly scored sentences also have a high score,
    # even if they don't contain highly scored words

    # sort the sentences in descending order of score
    sorted_sentences = sorted(zip(sentence_scores, enumerate(sentences)), reverse=True)

    # add top sentences to the summary. we keep track of sentences by index
    summary_length = 0
    summary_sentence_index_set: set[int] = set()
    for (score, (sentence_index, sentence)) in sorted_sentences:
        sentence_length = len(sentence)
        if summary_length + sentence_length <= max_summary_length:
            summary_sentence_index_set.add(sentence_index)
            summary_length += sentence_length
        else:
            break

    # construct the summary by joining the top sentences in the same order they appear
    summary = " ".join((
        sentences[sentence_index]
        for sentence_index in sorted(summary_sentence_index_set)
    ))

    return summary


#############################################################################################################
#  * Function:            summarizeTopic
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        03/28/2023

#  * Description:
#  * Returns a summary/description of a topic given the links. It will only summarize wiki links due to length
#  * and api limitations. the links should be the same or of similar topic or the summary not be focused.

#  * Parameters:
#  * links              list()              list of all the links to summarize
#############################################################################################################
def summarizeTopic(links, keywords: list = None) -> str:
    wikiLinks = set()

    # filters everything but wiki links and adds them to a list
    for item in links:
        if __isWiki__(item):
            wikiLinks.add(item)

    total_summary = ""

    # summarizes each link and consolidate them together
    for url in wikiLinks:
        page_content = asyncio.run(download_page(url))  # important: note that the call is async
        summary = __basic_summarize__(page_content, keywords)
        total_summary = total_summary + summary

    openai = OpenAI()
    response = asyncio.run(openai.summarize(total_summary))

    return response


#############################################################################################################
#  * Function:            __isWiki__
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        04/05/2023

#  * Description:
#  * Returns a bool value if the link provided is a wiki.
#  *

#  * Parameters:
#  * link               list()              link to analyze
#############################################################################################################
def __isWiki__(link):
    link = link.lower().split(".")
    for part in link[:-1]:
        if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
            return True

    return False
