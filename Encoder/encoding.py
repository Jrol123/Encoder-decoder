"""

"""
__all__ = ['encode']

DEFAULT_KEYWORD = "Depression"
SYM_INDEX = 65

def encode(keyword=DEFAULT_KEYWORD):
    for sym in keyword:
        print(ord(sym) - SYM_INDEX)
