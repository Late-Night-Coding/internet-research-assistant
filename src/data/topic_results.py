from data.url import URL
from data.url_category import URLCategory
from data.web_content import WebContent

class TopicResults:
    def __init__(self, topic_name: str, topic_description: str, url_list: list[URL]):
        self.topic_name = topic_name
        self.topic_description = topic_description
        self.url_list: list[URL] = list(url_list)

        self.__sort_links()

    #############################################################################################################
    #  * Function:            addTopics
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the name of the topic
    #############################################################################################################
    def get_topic_name(self) -> str:
        return self.topic_name

    #############################################################################################################
    #  * Function:            getTopicDescription
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the description/summary of the topic
    #############################################################################################################
    def get_topic_description(self) -> str:
        return self.topic_description

    #############################################################################################################
    #  * Function:            getURLs
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023

    #  * Description:
    #  * returns the list of URLs
    #############################################################################################################
    def get_urls(self):
        return self.url_list

    #############################################################################################################
    #  * Function:            __sort_links
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        04/07/2023

    #  * Description:
    #  * sort the links based on the category of the links
    #############################################################################################################
    def __sort_links(self) -> None:

        wikiLinks = list()
        youtubeLinks = list()
        socialLinks = list()
        otherLinks = list()

        for item in self.url_list:
            if item.category.name == "Wiki":
                wikiLinks.append(item)
            elif item.category.name == "Youtube":
                youtubeLinks.append(item)
            elif item.category.name == "Social Media":
                socialLinks.append(item)
            else:
                otherLinks.append(item)

        self.url_list = [*wikiLinks, *youtubeLinks, *socialLinks, *otherLinks]
