from model import converter

def convert(currency):
  while(True):
    inp = input('Enter text:')
    print(converter(inp,currency))

if __name__=='__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--currency', dest='currency', required=True)
    args = args_parser.parse_args()
    convert(currency=args.currency)
