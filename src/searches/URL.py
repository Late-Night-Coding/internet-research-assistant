from URLCategory import URLCategory

class URL:
    def __init__(self, link: str, category: URLCategory):
        self.link = link
        self.category = category

    #############################################################################################################
    #  * Function:            getLink
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the link stored
    #############################################################################################################
    def getLink(self) -> str:
        return self.link

    #############################################################################################################
    #  * Function:            getCategory
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023
    #  *
    #  * Description:
    #  * returns the category the url belongs to
    #############################################################################################################
    def getCategory(self) -> URLCategory:
        return self.category


