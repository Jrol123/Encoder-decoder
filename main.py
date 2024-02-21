from Decoder import *
from Encoder import *

input_text = input("")
res_e = encode(input_text)
print(res_e)
res_d = decode(res_e)
print(res_d)
