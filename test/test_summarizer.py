import pytest
from nlp.basic_summarizer import __basic_summarize__

@pytest.mark.parametrize("kwargs,expected_summary", [
    ({
        "content": "This is a sample paragraph. Notice that its length does not exceed the maximum, so there is no need to summarize.",
        "max_summary_length": 10000,
    }, "This is a sample paragraph. Notice that its length does not exceed the maximum, so there is no need to summarize."),

    ({
        "content": "Apple banana charlie. Dog apples cat. Dogs foxes wolves. Bear spider zombie.",
        "max_summary_length": 25
    }, "Dog apples cat."),

    ({
        "content": "",
        "max_summary_length": 25
    }, ""),

    ({
        "content": "Apple banana charlie. Dog apples cat. Dogs foxes wolves.",
        "keywords": ["fox"],
        "max_summary_length": 25
    }, "Dogs foxes wolves."),

    ({
        "content": "Apple cat banana charlie. Bear spider zombie. Dog apples cat. Dogs foxes wolves.",
        "max_summary_length": 45 
    }, "Apple cat banana charlie. Dog apples cat.")

])
def test_summarize(kwargs, expected_summary):
    assert __basic_summarize__(**kwargs, min_sent_len=0) == expected_summary