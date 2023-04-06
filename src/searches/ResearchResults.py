from searches.TopicResults import TopicResults


class ResearchResults:
    def __init__(self):
        self.topics = list()
        self.descriptions = list()

    #############################################################################################################
    #  * Function:            addTopics
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * creates a new topic with a name, description and list of url
    #############################################################################################################
    def addTopics(self, topic: str, description: str, URLlist: list) -> None:
        newTopic = TopicResults(topic, description, URLlist)
        self.topics.append(newTopic)

    #############################################################################################################
    #  * Function:            getTopics
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  *
    #############################################################################################################
    def getTopics(self, index=None, name=None) -> list:

        # return the entire thing
        if index is None and name is None:
            return self.topics

        # return the index of the topic
        elif index is not None:
            return self.topics[index]

        # if the name is not empty return the specific topic
        elif name is not None:
            for topic in self.topics:
                if topic.getTopicName == name:
                    return topic



