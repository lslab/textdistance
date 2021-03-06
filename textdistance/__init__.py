"""
TextDistance.
Compute distance between sequences.
30+ algorithms, pure python implementation, common interface. 
"""

# main package info
__title__ = 'TextDistance'
__version__ = '3.0.2'
__author__ = 'Gram Orsinium'
__license__ = 'LGPL 3.0'


# version synonym
VERSION = __version__


# facade
from .interfaces import distance    # noQA
from .utils import *                # noQA
from .algorithms import *           # noQA
