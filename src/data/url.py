from data.url_category import URLCategory

class URL:
    def __init__(self, link: str, category: URLCategory):
        self.link = link
        self.name = link.split("//")[1].split("/")[0].replace("www.", "")
        self.category = category

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



