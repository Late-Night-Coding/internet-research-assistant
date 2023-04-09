from data.url import URL
from data.url_category import URLCategory


class TopicResults:
    def __init__(self, topic_name: str, topic_description: str, url_list: list[str]):
        self.topic_name = topic_name
        self.topic_description = topic_description
        self.url_list: list[URL] = list()

        # create categories
        self.wiki_cat = URLCategory("Wiki", "54")
        self.youtube_cat = URLCategory("Youtube", "1")
        self.social_media_cat = URLCategory("Social Media", "185")
        self.other_cat = URLCategory("Other", "108")

        # add all the links to the url
        for link in url_list:
            self.url_list.append(URL(link, self.__classify_link(link)))

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
    #  * Function:            __classify_link
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/29/2023

    #  * Description:
    #  * Assigns links to categories based on the domain of the link
    #  * returns the URLCategory class
    #############################################################################################################
    def __classify_link(self, link: str):
        link = link.lower().split(".")
        for part in link[:-1]:
            if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
                return self.wiki_cat
            elif "youtube" in part:
                return self.youtube_cat
            elif ("twitter" in part) or ("facebook" in part) or ("instagram" in part):
                return self.social_media_cat

        return self.other_cat

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
