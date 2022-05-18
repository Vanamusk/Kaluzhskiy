import argparse
import sys
import json

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--country')
    parser.add_argument('--petal_colour',choices= ['R','W','Y','V','B'])
    parser.add_argument('--stem_length',type = int)
    parser.add_argument('--with_thorns',action="store_true")
    parser.add_argument('--companion_plants', nargs = '+',default= None)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    data = {"name": namespace.name,
            "country": namespace.country,
            "petal_colour": namespace.petal_colour,
            "stem_length": namespace.stem_length,
            "with_thorns": namespace.with_thorns,
            "companion_plants": namespace.companion_plants}
    with open("./journal.txt", 'a') as file:
        json.dump(data, file)

