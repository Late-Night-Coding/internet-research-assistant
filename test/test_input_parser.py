from nlp.input_parser import InputParser



def test_single_word():
    word_to_parse = "baseball"
    tokens, tags = InputParser().parse(word_to_parse)
    assert tokens == ["baseball"] and tags == [('baseball', 'NN')]

def test_sentence():
    sentence_to_parse = "what is the capital of the United States?"
    tokens, tags = InputParser().parse(sentence_to_parse)
    assert tokens == ["capital", "united", "state"] and tags == [('capital', 'NN'), ('united', 'VBD'), ('state', 'NN')]

def test_nonsense():
    nonsense_to_parse = "oibaoeinh oibanf iuvagu"
    tokens, tags = InputParser().parse(nonsense_to_parse)
    print(tags)
    assert tokens == ["oibaoeinh", "oibanf", "iuvagu"] and tags == [('oibaoeinh', 'JJ'), ('oibanf', 'NN'), ('iuvagu', 'NN')]