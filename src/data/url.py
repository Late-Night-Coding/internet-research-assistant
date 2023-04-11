from data.url_category import URLCategory, classify_link
from data.web_content import WebContent


# Factory method for URLs.
def create_url_from_web_content(web_content: WebContent):
    return URL(
        link=web_content.url,
        category=classify_link(web_content.url),
        title=web_content.page_title
    )

class URL:
    def __init__(self, link: str, category: URLCategory, title: str):
        self.link = link
        self.category = category

        self.name = self.__title_shortener(title) + ": " + link.split("//")[1].split("/")[0].replace("www.", "")


    #############################################################################################################
    #  * Function:            getLink
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the link stored
    #############################################################################################################
    def get_link(self) -> str:
        return self.link

    #############################################################################################################
    #  * Function:            getCategory
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the category the url belongs to
    #############################################################################################################
    def get_category(self) -> URLCategory:
        return self.category

    #############################################################################################################
    #  * Function:            __title_shortener
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        04/10/2023
    #  *
    #  * Description:
    #  * returns a shortened version of the title if its too long and returns something if there is no title
    #############################################################################################################
    def __title_shortener(self, title):
        if title:
            if len(title) > 45:
                new_text = ""
                texts = title.split(" ")
                i = 0

                while len(new_text) < 50 and i < len(texts):
                    new_text += texts[i] + " "
                    i += 1
                new_text += "..."
                return new_text
            else:
                return title
        else:
            return ""
