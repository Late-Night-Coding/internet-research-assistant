import asyncio
from data.search_history import SearchHistory
from openai_api import OpenAI

def test_summarize():
    open_ai = OpenAI()
    dog_wiki_summary = """The dog (Canis familiaris[4][5] or Canis lupus familiaris[5]) is a domesticated descendant of the wolf.
        Also called the domestic dog, it is derived from the extinct Pleistocene wolf,[6][7] and the modern wolf is the dog's nearest living relative.[8]
        Dogs were the first species to be domesticated[9][8] by hunter-gatherers over 15,000 years ago[7] before the development of agriculture."""
    dog_description = asyncio.run(open_ai.summarize("dog", dog_wiki_summary))

    assert isinstance(dog_description, str)
    assert len(dog_description) > 0
    
    print(f"Dear tester, please validate this description of 'dog':\n{dog_description}")

def test_non_recursive_get_search_terms():
    open_ai = OpenAI()
    search_history = SearchHistory("animal", "id1")

    search_terms = asyncio.run(open_ai.get_search_keywords(search_history))

    assert isinstance(search_terms, list)
    assert len(search_terms) > 1
    assert isinstance(search_terms[0], str)
    
    print(f"Dear tester, please validate this set of search terms for 'animal':\n{str(search_terms)}")

def test_recursive_get_search_terms():
    open_ai = OpenAI()
    parent_topic = 'baseball'
    child_topic = 'teams'
    search_history = SearchHistory(parent_topic, "id1")
    search_history.append_keyword(child_topic)

    search_terms = asyncio.run(open_ai.get_search_keywords(search_history))

    assert isinstance(search_terms, list)
    assert len(search_terms) > 1
    assert isinstance(search_terms[0], str)
    
    print(f"Dear tester, please validate this set of search terms for '{parent_topic} > {child_topic}':\n{str(search_terms)}")
