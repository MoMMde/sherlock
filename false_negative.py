import argparse
import json

import sherlock.sherlock as sherlock
from .sherlock.sites  import SitesInformation
from .sherlock.result import QueryStatus

parser = argparse.ArgumentParser('Simple Argument parser')
parser.add_argument('-f', '--file', help='File to read', required=False)
parser.add_argument('-o', '--overwrite', help='Overwrite existing data file', required=False, default=True)

if __name__ == '__main__':
    args = parser.parse_args()
    overwrite = args.overwrite
    sites = SitesInformation(args.file)
    for site in sites:
        if site.