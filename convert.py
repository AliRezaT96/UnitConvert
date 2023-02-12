from model.model import currency_converter
import argparse


def convert(currency):
  while(True):
    inp = input('Enter text:')
    out = currency_converter(inp,currency)
    print(out)

if __name__=='__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--currency', dest='currency', required=True)
    args = args_parser.parse_args()
    convert(currency=args.currency)
