#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from lib.dbm import Dbm

# Set up argument parser
argument_parser = argparse.ArgumentParser()

def list_entries(entries_to_print, args):
    """Prints an appealing representation of entries"""

    for key, value in vars(args).items():
        try:
            entries_to_print = [entry for entry in entries_to_print if getattr(entry, key) in value]
        except:
            pass

    print()
    print("Printing entries:")
    print()
    for entry in entries_to_print:
        if args.export:
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
        database_contents = my_dbm.read_database()
    except FileNotFoundError:
        print("Get the database ready, maaan!")
        sys.exit(1)

    list_entries(database_contents, args)


if __name__ == "__main__":
    run()
