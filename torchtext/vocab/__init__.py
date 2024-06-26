import warnings
import torchtext
if torchtext._WARN:
    warnings.warn(torchtext._TORCHTEXT_DEPRECATION_MSG)

from .vectors import CharNGram, FastText, GloVe, pretrained_aliases, Vectors
from .vocab import Vocab
from .vocab_factory import build_vocab_from_iterator, vocab

__all__ = [
    "Vocab",
    "vocab",
    "build_vocab_from_iterator",
    "GloVe",
    "FastText",
    "CharNGram",
    "pretrained_aliases",
    "Vectors",
]
