#!/usr/bin/env python

import sys
from query import *
from pprint import pprint

if __name__ == "__main__":
    result = query(sys.argv[1])
    pprint(result)
