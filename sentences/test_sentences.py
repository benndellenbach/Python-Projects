from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = get_determiner_list(1)

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = get_determiner_list(2)

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

# 1. Test the single nouns

    single_nouns = get_noun_list(1)

    for _ in range(4):
        word = get_noun(1)

        assert word in single_nouns

 # 2. Test the plural nouns

    plural_nouns = get_noun_list(2)

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():

# 1. Test the past verbs
    past_verbs = ["drank",
            "ate",
            "grew",
            "laughed",
            "thought",
            "ran",
            "slept",
            "talked",
            "walked",
            "wrote"]

    for _ in range(4):
        word = get_verb(1, "past")
        assert word in past_verbs

 # 2. Test the present single verbs

    present_single_verbs = [ "drinks",
                "eats",
                "grows",
                "laughs",
                "thinks",
                "runs",
                "sleeps",
                "talks",
                "walks",
                "writes"]

    for _ in range(4):
        word = get_verb(1, "present")
        assert word in present_single_verbs

# 3. Test the present plural verbs

    present_plural_verbs = ["drink",
                "eat",
                "grow",
                "laugh",
                "think",
                "run",
                "sleep",
                "talk",
                "walk",
                "write"]

    for _ in range(4):
        word = get_verb(2, "present")
        assert word in present_plural_verbs

# 4. Test the future verbs

    future_verbs = ["will drink",
            "will eat",
            "will grow",
            "will laugh",
            "will think",
            "will run",
            "will sleep",
            "will talk",
            "will walk",
            "will write"]

    for _ in range(4):
        word = get_verb(1, "future")
        assert word in future_verbs

def test_get_preposition():
# Testing prepositions
    test_prepositions = get_preposition_list()
    for _ in range(4):
        word = get_preposition()
        assert word in test_prepositions

def test_get_prepositional_phrase():

    #1. Test the single prepositional phrase
    for _ in range(4):

        word_list = get_prepositional_phrase(1).split(" ")
        word_count = len(word_list)
        test_prep = str(word_list[0])
        test_det = str(word_list[1])
        test_noun = str(word_list[2])

        assert word_count == 3
        assert test_prep in get_preposition_list()
        assert test_det in get_determiner_list(1)
        assert test_noun in get_noun_list(1)

    #2. Test the plural prepositional phrase
    for _ in range(4):

        word_list = get_prepositional_phrase(2).split(" ")
        word_count = len(word_list)
        test_prep = str(word_list[0])
        test_det = str(word_list[1])
        test_noun = str(word_list[2])

        assert word_count == 3
        assert test_prep in get_preposition_list()
        assert test_det in get_determiner_list(2)
        assert test_noun in get_noun_list(2)

def get_noun_list(quantity):

    single_nouns = ["bird",
            "boy",
            "car",
            "cat",
            "child",
            "dog",
            "girl",
            "man",
            "rabbit",
            "woman"]

    plural_nouns = ["birds",
            "boys",
            "cars",
            "cats",
            "children",
            "dogs",
            "girls",
            "men",
            "rabbits",
            "women"]
    
    if quantity == 1:
        return single_nouns

    else:
        return plural_nouns

def get_determiner_list(quantity):

    single_determiners = ["a", "one", "the"]
    plural_determiners = ["two", "some", "many", "the"]

    if quantity == 1:
        return single_determiners
    else:
        return plural_determiners

def get_preposition_list():

        prepositions = [
        "about",
        "above",
        "across",
        "after",
        "along",
        "around",
        "at",
        "before",
        "behind",
        "below",
        "beyond",
        "by",
        "despite",
        "except",
        "for",
        "from",
        "in",
        "into",
        "near",
        "of",
        "off",
        "on",
        "onto",
        "out",
        "over",
        "past",
        "to",
        "under",
        "with",
        "without",
        ]

        return prepositions


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])