from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

##Positional arguments
parser.add_argument('a',type=int, help='The base value.')
parser.add_argument('b', type=int, help = 'The exponent value.')

##Optional arguments

parser.add_argument('-v','--verbose',action='count',
                    help='Provides a verbose description. Use -vv for extra verbose')

args:Namespace = parser.parse_args()
result : int = args.a ** args.b

if args.verbose ==1:
    print(f"The result is {result}")
elif args.verbose == 2:
    print(f"{args.a} ** {args.b} = {result}")
else:
    print(result)

#https://docs.python.org/3/howto/argparse.html
