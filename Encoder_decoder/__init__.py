"""
To be written
"""
__author__ = 'Artemii Popovkin'
__version__ = '0.01'
__license__ = 'MIT'
__email__ = 'angap4@gmail.com'

__github__ = 'https://github.com/Jrol123/Encoder-decoder'

from .Encoder import *
from .Decoder import *
from .test import *
__all__ = ['Encoder', 'Decoder']


def greetings():
    """
    Greetings message

    """
    print(f'Hello!\n'
          f'It`s {__author__} speaking!\n'
          f'Right now you are using Encoder_decoder version of: {__version__}!\n\n'
          f'Have a good day!')
