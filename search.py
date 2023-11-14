#!/usr/bin/env python

import argparse
from query import *
from pprint import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word", type=str, default="word", help="The word that you are searching for.")
    args = parser.parse_args()
    result = query(args.word)
    pprint(result)
