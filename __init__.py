"""
To be written
"""
__author__ = 'Artemii Popovkin'
__email__ = 'angap4@gmail.com'
__github__ = 'https://github.com/Jrol123/Encoder-decoder'

__license__ = 'MIT'
__version__ = '0.015'

from .Encoder import *
from .Decoder import *

__all__ = ['encode']  # Перечисление всех функций, доступных извне.


def greetings():
    """
    Greetings message

    """
    print(f'Hello!\n'
          f'It`s {__author__} speaking!\n'
          f'Right now you are using Encoder_decoder version of: {__version__}!\n\n'
          f'Have a good day!')
