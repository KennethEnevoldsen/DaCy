import os

import spacy

from .download import download_model, DEFAULT_CACHE_DIR

def load_model(model, path=DEFAULT_CACHE_DIR):
    """
    model (str): use dacy_models() to see all available models
    """
    download_model(model, path)
    path = os.path.join(path, model)
    spacy.load(path)