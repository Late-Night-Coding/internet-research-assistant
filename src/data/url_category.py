import random

class URLCategory:
    def __init__(self, name: str, color=None):
        self.name = name
        if color is None:
            self.color = random.randint(0, 359)
        else:
            self.color = color

    def get_color(self):
        return self.color

    def get_category_name(self):
        return self.name


# create categories
wiki_cat = URLCategory("Wiki", "54")
youtube_cat = URLCategory("Youtube", "1")
social_media_cat = URLCategory("Social Media", "185")
other_cat = URLCategory("Other", "108")

#############################################################################################################
#  * Function:            classify_link
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        03/29/2023

#  * Description:
#  * Assigns links to categories based on the domain of the link
#  * returns the URLCategory class
#############################################################################################################
def classify_link(link: str):
    link = link.lower().split(".")
    for part in link[:-1]:
        if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
            return wiki_cat
        elif "youtube" in part:
            return youtube_cat
        elif ("twitter" in part) or ("facebook" in part) or ("instagram" in part):
            return social_media_cat

    return other_cat