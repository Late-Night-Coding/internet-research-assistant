from data.research_results import ResearchResults
from data.url_category import URLCategory
from data.url import URL
from data.topic_results import TopicResults

wiki_cat = URLCategory("Wiki", color=38)
youtube_cat = URLCategory("Youtube", color=1)

football_wiki = URL("https://en.wikipedia.org/wiki/Football", category=wiki_cat, title="Football")
football_youtube = URL("https://www.youtube.com/watch?v=3OXO3oymegU", category=youtube_cat, title="Football youtube")
soccer_wiki = URL("https://en.wikipedia.org/wiki/Association_football", category=wiki_cat, title="Soccer wiki")


def test_call_add_once():
    result = ResearchResults()
    topic_football = TopicResults(topic_name="Football",
                                  topic_description="Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.",
                                  url_list=[football_wiki, football_youtube])

    result.add_topic(topic_football)

    result_list = result.get_topics()

    assert result_list[0].topic_name == "football"


def test_call_zero():
    result = ResearchResults()

    assert result == result



def test_call_twice():
    result = ResearchResults()
    topic_football = TopicResults(topic_name="Football",
                                  topic_description="Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.",
                                  url_list=[football_wiki, football_youtube])

    topic_soccer = TopicResults(topic_name="Soccer",
                                topic_description="Soccer in the United States is run by multiple organizations.[8] The United States Soccer Federation (USSF) governs most levels of soccer in the country, including the national teams",
                                url_list=[soccer_wiki])

    result.add_topic(topic_football)
    result.add_topic(topic_soccer)

    topics = result.get_topics()

    assert topics[0].topic_name == "Football" and topics[0].topic_description == "Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal."
    assert topics[0].url_list[0].link == "https://en.wikipedia.org/wiki/Football" and topics[0].url_list[0].name == "Football: en.wikipedia.org"
    assert topics[0].url_list[0].category.name == "Wiki" and topics[0].url_list[0].category.color == 38

    assert topics[0].topic_name == "Football" and topics[0].topic_description == "Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal."
    assert topics[0].url_list[1].link == "https://www.youtube.com/watch?v=3OXO3oymegU" and topics[0].url_list[1].name == "Football youtube: youtube.com"
    assert topics[0].url_list[1].category.name == "Youtube" and topics[0].url_list[1].category.color == 1

    assert topics[1].topic_name == "Soccer" and topics[1].topic_description == "Soccer in the United States is run by multiple organizations.[8] The United States Soccer Federation (USSF) governs most levels of soccer in the country, including the national teams"
    assert topics[1].url_list[0].link == "https://en.wikipedia.org/wiki/Association_football" and topics[1].url_list[0].name == "Soccer wiki: en.wikipedia.org"
    assert topics[1].url_list[0].category.name == "Wiki" and topics[1].url_list[0].category.color == 38
