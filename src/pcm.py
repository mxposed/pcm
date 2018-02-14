#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################
#                         #
#     Import section      #
#                         #
###########################


import re
import uuid
import pickle


###########################
#                         #
#  Global To Do section   #
#                         #
###########################


# Please note that these might be subject to change!

# TODO: Make programme use `argparse` to properly run from command line
# TODO: Insert assertions and exceptions where sensible
# TODO: Write unit tests
# TODO: Move to OOP
# TODO: Modularise
# TODO: Extend with notes, favourites, tags, search, update,


###########################
#                         #
#  Configuration section  #
#                         #
###########################


# TODO: Should make use of `configparser` instead

DATA_FILE = "database.pickle"

# Variable initialisation
all_entries = []


###########################
#                         #
#    Function section     #
#                         #
###########################

def clear_library():
    all_entries.clear()


def parse_bibtex_file(bibtex_file):
    """Returns a dictionary of a parsed entry for a given BibTeX file"""
    with open(bibtex_file, 'r') as f:
        file_contents = f.read()
    return parse_bibtex_entry(file_contents)


def parse_bibtex_entry(entry):
    """Returns a dictionary of a parsed entry for a given BibTeX entry"""

    new_entry = {}

    field_pairs  = re.findall(r"\s{3}(.*?)={(.*?)}", entry)
    bibtex_class = re.findall(r"(?<=@).*?(?={)",     entry)[0]
    cite_key     = re.findall(r"@.*{(.*),",          entry)[0]

    # Set fields
    for (key, value) in field_pairs:
        new_entry[key] = value

    # Set identifiers
    new_entry["uuid"]         = str(uuid.uuid4())
    new_entry["bibtex_class"] = bibtex_class
    new_entry["cite_key"]     = cite_key

    return new_entry


def add_entry(bibtex_file):
    """Adds an entry for the given BibTeX file to the runtime list of entries"""
    all_entries.append(parse_bibtex_file(bibtex_file))


def format_entry(entry):
    result = 'Title: {}\n'.format(entry['title'])
    result += 'Author: {}\n'.format(entry['author'])
    if entry['bibtex_class'] == 'online':
        result += 'URL: {}\n'.format(entry['url'])
    result += '-----\n'
    result += 'BibTeX Class: {}\n'.format(entry['bibtex_class'])
    result += 'UUID: {}\n'.format(entry['uuid'])
    result += '=====\n'
    return result


def list_entries(entries_to_print):
    """Prints an appealing representation of entries"""
    print()
    print("Printing all entries:")
    print()
    for entry in entries_to_print:
        print(format_entry(entry))
    print("Done printing.")


def export_entries(entries_to_export):
    """Essentially a 'reverse parser'"""
    pass


def delete_entry(uuid_of_entry_to_delete):
    for entry in all_entries:
        if entry["uuid"] == uuid_of_entry_to_delete:
            all_entries.remove(entry)


def write_database(entries_to_store):
    with open(DATA_FILE, 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(entries_to_store, f, pickle.HIGHEST_PROTOCOL)


def read_database():
    with open(DATA_FILE, 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        return pickle.load(f)


###########################
#                         #
# Main execution section  #
#                         #
###########################


if __name__ == "__main__":

    # Add and save

    """
    add_entry("../Resources/scholar_1.txt")
    add_entry("../Resources/scholar_2.txt")

    list_entries(all_entries)

    write_database(all_entries)
    """

    # Restore list

    """
    all_entries = read_database()
    
    list_entries(all_entries)
    """

    # Delete an entry and save changes

    """
    my_uuid_to_delete = None
    delete_entry(my_uuid_to_delete)

    list_entries(all_entries)
    
    write_database(all_entries)
    """
