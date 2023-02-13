from model.model import currency_converter, size_converter
from preprocess.preprocess import cleaning
import argparse


def convert_price(currency):
  while(True):
    inp = input('Enter text:')
    out = currency_converter(cleaning(inp),currency)
    print(out)

def convert_size():
  while (True):
    inp = input('Enter Text:')
    out = size_converter(cleaning(inp))
    print(out)

if __name__=='__main__':

    convert_size()

# if __name__=='__main__':

#     args_parser = argparse.ArgumentParser()
#     args_parser.add_argument('--currency', dest='currency', required=True)
#     args = args_parser.parse_args()
#     convert_price(currency=args.currency)
