#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from lib.dbm import Dbm

# Set up argument parser
argument_parser = argparse.ArgumentParser()


def set_up_argparse():
    argument_parser.description = "Deletes one of more entries from the database given by uuid"

    argument_parser.add_argument(
        'uuid',
        nargs='+',
        help="ID of the entry or entries to delete"
    )

    argument_parser.add_argument(
        "-e",
        "--echo",
        help="Echo back which entry we're deleting"
    )


def run():
    # Set up argument parser
    set_up_argparse()

    # Print full help text if no arguments given
    if len(sys.argv) == 1:
        argument_parser.print_help()
        sys.exit(1)
    # Otherwise print args we're given
    else:
        args = argument_parser.parse_args()

    # Initialise "database connection"
    my_dbm = Dbm()

    # Get all current contents
    old_database_contents = my_dbm.read_database()

    # Filter out entr(y|ies) we wish to delete
    new_database_contents = [entry for entry in old_database_contents if entry.uuid not in args.uuid]

    # Write back modified list of entries
    my_dbm.write_database(new_database_contents)


if __name__ == "__main__":
    run()
