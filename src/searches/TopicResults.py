from URL import URL
from URLCategory import URLCategory

class TopicResults:
    def __init__(self, topicName, topicDescription, URLlist: list):
        self.topicName = topicName
        self.topicDescription = topicDescription
        self.URLlist = list()
        self.wikiCat = URLCategory("Wiki")
        self.youtubeCat = URLCategory("Youtube", "#FF6961")
        self.socialMedia = URLCategory("Social Media")
        self.otherCat = URLCategory("Other")

        # add all the links to the url
        for link in URLlist:
            self.URLlist.append(URL(link, self.__linkClassifier__(link)))

    #############################################################################################################
    #  * Function:            addTopics
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the name of the topic
    #############################################################################################################
    def getTopicName(self) -> str:
        return self.topicName

    #############################################################################################################
    #  * Function:            getTopicDescription
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the description/summary of the topic
    #############################################################################################################
    def getTopicDescription(self) -> str:
        return self.topicDescription

    #############################################################################################################
    #  * Function:            getURLs
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023

    #  * Description:
    #  * returns the list of URLs
    #############################################################################################################
    def getURLs(self):
        return self.URLlist

    #############################################################################################################
    #  * Function:            __linkClassifier__
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/29/2023

    #  * Description:
    #  * Assigns links to categories based on the domain of the link
    #  * returns the URLCategory class
    #############################################################################################################
    def __linkClassifier__(self, link: str):
        link = link.lower().split(".")
        for part in link:
            if "wiki" or "fandom" in part:
                return self.wikiCat
            elif "youtube" in part:
                return self.youtubeCat
            elif "twitter" or "facebook" or "instagram" in part:
                return self.socialMedia
            else:
                return self.otherCat