#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import re
import uuid

from lib.entries import *

from lib.dbm import Dbm

# Set up argument parser
argument_parser = argparse.ArgumentParser()


def parse_bibtex_file(bibtex_file):
    """Returns a dictionary of a parsed entry for a given BibTeX file"""
    with open(bibtex_file, 'r') as f:
        file_contents = f.read()

    return parse_bibtex_entry(file_contents)


def parse_bibtex_entry(entry):
    """Returns a dictionary of a parsed entry for a given BibTeX entry"""

    # We start out with a dictionary, but will turn it into a proper object further down
    new_entry = {}

    field_pairs = re.findall(r"\s{3}(.*?)={(.*?)}", entry)
    bibtex_class = re.findall(r"(?<=@).*?(?={)", entry)[0]
    cite_key = re.findall(r"@.*{(.*),", entry)[0]

    # Set fields
    for (key, value) in field_pairs:
        new_entry[key] = value

    # Set identifiers
    new_entry["uuid"] = str(uuid.uuid4())
    new_entry["bibtex_class"] = bibtex_class
    new_entry["cite_key"] = cite_key

    # This'll simplify nicely once we use **kwargs, as we can pre-populate that list instead of repeating ourselves!
    if bibtex_class == 'book':
        new_entry = Book(new_entry['uuid'],
                         new_entry['author'],
                         new_entry['title'],
                         new_entry['cite_key'],
                         new_entry['year'],
                         new_entry['publisher'])

    elif bibtex_class == 'article':
        new_entry = Article(new_entry['uuid'],
                            new_entry['author'],
                            new_entry['title'],
                            new_entry['cite_key'],
                            new_entry['journal'],
                            new_entry['volume'])

    elif bibtex_class == 'online':
        new_entry = Online(new_entry['uuid'],
                           new_entry['author'],
                           new_entry['title'],
                           new_entry['cite_key'],
                           new_entry['url'])

    return new_entry


def set_up_argparse():
    argument_parser.description = "Adds an entry for the given BibTeX file to the database"

    argument_parser.add_argument(
        'file',
        metavar='file',
        help="BibTeX file to add"
    )

    argument_parser.add_argument(
        '-n',
        "--note",
        nargs="+",
        help="Attach this note or these notes to the entry"
    )

    argument_parser.add_argument(
        '-t',
        "--tag",
        dest='tags',
        nargs="+",
        help="Tag the entry"
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
    # TODO: Check if database can actually be read. Otherwise create an empty one!
    db = my_dbm.read_database()

    # Add new entry/entries to previous database contents
    entry = parse_bibtex_file(args.file)
    db.entries.append(
        entry
    )

    for tag_name in args.tags:
        tag = Tag(tag_name)
        entry.add_tag(tag)
        db.tags.add(tag)

    # Write back modified list of entries
    my_dbm.write_database(db)


if __name__ == "__main__":
    run()
