#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from lib.dbm import Dbm


def run():
    my_dbm = Dbm()

    # Get all current contents
    try:
        db = my_dbm.read_database()
        print("You already have a database here")
        sys.exit(1)
    except FileNotFoundError:
        pass

    my_dbm.write_database([])


if __name__ == "__main__":
    run()
