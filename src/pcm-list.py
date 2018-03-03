#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from lib.dbm import Dbm

# Set up argument parser
from lib.entries import Tag

argument_parser = argparse.ArgumentParser()


def list_entries(entries_to_print, author=None, tags=None, export=False):
    """Prints an appealing representation of entries"""

    filtered_entries = []
    for entry in entries_to_print:
        if author:
            if entry.author not in author:
                continue
        if tags:
            tags = set([Tag(name) for name in tags])
            if not tags.issubset(entry.tags):
                continue
        filtered_entries.append(entry)

    print()
    print("Printing entries:")
    print()
    for entry in filtered_entries:
        if export:
            print(entry.export_representation())
        else:
            print(str(entry))
    print()
    print("Done printing.")


def set_up_argparse():
    argument_parser.description = "List entries in database dependent on query parameters"

    argument_parser.add_argument(
        '--author',
        nargs=1,
        help="Name of the author to search for"
    )

    argument_parser.add_argument(
        '--tags',
        dest='tags',
        nargs='+',
        help='Tags for filtering'
    )

    argument_parser.add_argument(
        "-e",
        "--export",
        action="store_true",
        help="If this flag is set, the output will be displayed in a machine-readable format instead "
             "of a user-friendly format"
    )


def run():
    # Set up argument parser
    set_up_argparse()

    # Print full help text if no arguments given
    args = argument_parser.parse_args()

    # Initialise "database connection"
    my_dbm = Dbm()

    # Get all current contents
    try:
        library = my_dbm.read_database()
    except FileNotFoundError:
        print("Get the database ready, maaan!")
        sys.exit(1)

    list_entries(library.entries, author=args.author, tags=args.tags, export=args.export)


if __name__ == "__main__":
    run()
