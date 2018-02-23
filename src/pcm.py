#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################
#                         #
#  Global To Do section   #
#                         #
###########################

# Please note that these might be subject to change!

# TODO: Insert assertions and exceptions where sensible
# TODO: Write additional unit tests
# TODO: Extend with notes, favourites, tags, search, update, ...


###########################
#                         #
#    Function section     #
#                         #
###########################

def clear_library():
    all_entries.clear()


###########################
#                         #
# Main execution section  #
#                         #
###########################

if __name__ == "__main__":

    # Create database

    """
    my_dbm = Dbm()

    # Add and save

    add_entry("../Resources/scholar_1.txt")
    add_entry("../Resources/scholar_2.txt")
    add_entry("../Resources/scholar_3.txt")

    list_entries(all_entries)

    my_dbm.write_database(all_entries)

    """

    # TODO: Entries below still use the old style of accessing the database

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
