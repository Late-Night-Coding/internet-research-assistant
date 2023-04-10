import json

from flask import jsonify

from data.topic_results import TopicResults


class ResearchResults:
    def __init__(self):
        self.topics: list[TopicResults] = list()

    #############################################################################################################
    #  * Function:            addTopic
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * creates a new topic with a name, description and list of url
    #############################################################################################################
    def add_topic(self, topic: str, description: str, URLlist: list, page_contents: list) -> None:
        newTopic = TopicResults(topic, description, URLlist, page_contents)
        self.topics.append(newTopic)

    #############################################################################################################
    #  * Function:            getTopics
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  *
    #############################################################################################################
    def get_topics(self, index=None, name=None):

        # return the entire thing
        if index is None and name is None:
            return self.topics

        # return the index of the topic
        elif index is not None:
            return self.topics[index]

        # if the name is not empty return the specific topic
        elif name is not None:
            for topic in self.topics:
                if topic.get_topic_name == name:
                    return topic
