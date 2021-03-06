from dacy.sentiment import (
    add_berttone_subjectivity,
    add_berttone_polarity,
    add_bertemotion_laden,
    add_bertemotion_emo,
)

import spacy


def test_add_berttone_subjectivity():
    nlp = spacy.blank("en")
    nlp = add_berttone_subjectivity(nlp)
    texts = [
        "Analysen viser, at økonomien bliver forfærdelig dårlig",
        "Jeg tror alligvel, det bliver godt",
    ]
    actual = ["objective", "subjective"]
    docs = nlp.pipe(texts)
    for d, a in zip(docs, actual):
        assert d._.subjectivity == a


def test_add_berttone_polarity():
    nlp = spacy.blank("en")
    nlp = add_berttone_polarity(nlp)

    texts = [
        "Analysen viser, at økonomien bliver forfærdelig dårlig",
        "Jeg tror alligvel, det bliver godt",
    ]
    docs = nlp.pipe(texts)

    l = [d for d in docs]
    # text 0 should be more negative that text 1
    assert l[0]._.polarity_prop["prop"][0] < l[1]._.polarity_prop["prop"][0]


def test_add_bertemotion_laden():
    nlp = spacy.blank("en")
    nlp = add_bertemotion_laden(nlp)


def test_add_bertemotion_emo():
    nlp = spacy.blank("en")
    nlp = add_bertemotion_emo(nlp)
    doc = nlp("Har i set at Tesla har landet en raket på månen? Det er vildt!!")
    assert doc._.emotion == "Overasket/Målløs"
