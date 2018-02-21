import sys
import argparse

from lib.dbm import Dbm

# Set up argument parser
argument_parser = argparse.ArgumentParser()

# Read database contents
database_contents = Dbm.read_database()


def set_up_argparse():
    argument_parser.description = "List entries in database dependent on query parameters"

    argument_parser.add_argument(
        '--author',
        help="Name of the author to search for"
    )


def run():
    # Print full help text if no arguments given
    if len(sys.argv) == 1:
        argument_parser.print_help()
        sys.exit(1)
    # Otherwise print args we're given
    else:
        args = argument_parser.parse_args()


if __name__ == "__main__":
    run()
