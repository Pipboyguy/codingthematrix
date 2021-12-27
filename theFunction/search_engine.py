# Task 0.6.6

import string
from itertools import chain
from typing import Any, List


def remove_punctuation(doc: str) -> str:

    return doc.translate(str.maketrans("", "", string.punctuation))


def makeInverseIndex(strlist: List[str]) -> dict[str:int]:
    """
    Constructs an inverse index from the given list of strings

    :param strlist: list of strings (documents)
    :returns: dictionary that maps each word to the set
              consisting of the document numbers of
              documents in which that word appears.
    """

    ## create a word dictionary
    word_dictionary = set(
        list(chain(*map(lambda x: remove_punctuation(x).lower().split(), strlist)))
    )

    # remove single letter words
    word_dictionary = filter(lambda x: len(x) > 1, word_dictionary)
    # order alphabetically
    word_dictionary = sorted(word_dictionary)

    reverse_index = {
        word: [i for i, doc in enumerate(strlist) if word in doc.lower()]
        for word in word_dictionary
    }

    return reverse_index


def orSearch(inverseIndex: int, query: List[str]) -> set[str]:
    """
    orSearch(inverseIndex, query) which takes an inverse index and a list of words
    query, and returns the set of document numbers specifying all documents that
    conain any of the words in query.
    """

    return set(
        chain(
            *[
                index
                for (word, index) in inverseIndex.items()
                if word in set(map(lambda x: x.lower(), query))
            ]
        )
    )


def andSearch(inverseIndex: int, query: List[str]) -> set[str]:
    """
    Write a procedure andSearch(inverseIndex, query) which takes an inverse
    index and a list of words query, and returns the set of document numbers
    specifying all documents that contain all of the words in query.
    """

    return set.intersection(
        *map(
            set,
            (
                index
                for (word, index) in inverseIndex.items()
                if word in set(map(lambda x: x.lower(), query))
            ),
        )
    )
